import xarray as xr
import geopandas as gpd
from pathlib import Path
import warnings
import numpy as np
import rioxarray

def clip_to_europe(ds: xr.Dataset, shapefile_path: str) -> xr.Dataset:
    """
    Clips an xarray Dataset to the European continent using a shapefile.
    """
    import warnings
    import geopandas as gpd
    from rioxarray import exceptions as rio_exceptions

    # Load Europe shapefile
    europe_shape = gpd.read_file(shapefile_path)

    print("Shapefile bounds:", europe_shape.bounds)
    print("Dataset CRS:", ds.rio.crs)

    # Check if shapefile has a CRS; if not, assign it
    if europe_shape.crs is None:
        warnings.warn("Shapefile CRS is missing. Assigning EPSG:3035 (ETRS89 / LAEA Europe).")
        europe_shape = europe_shape.set_crs(epsg=3035)

    print("Shapefile bounds:", europe_shape.bounds)
    print("Dataset CRS:", ds.rio.crs)

    # Reproject to WGS84
    europe_shape = europe_shape.to_crs("EPSG:4326")

    # Ensure dataset CRS
    try:
        if not ds.rio.crs:
            ds = ds.rio.write_crs("EPSG:4326")
    except rio_exceptions.NoCRS:
        ds = ds.rio.write_crs("EPSG:4326")

    # Clip the dataset
    masked_data = ds.rio.clip(europe_shape.geometry, europe_shape.crs, drop=True)

    if masked_data.isnull().all():
        raise ValueError("Clipping resulted in an empty dataset. Check shapefile or dataset CRS.")

    return masked_data

def calc_windspeed(ds: xr.Dataset) -> xr.Dataset:
    """Calculate wind speed."""
    return np.sqrt(ds["u10"]**2 + ds["v10"]**2)

def calc_pv_pot(ds: xr.Dataset) -> xr.Dataset:
    """Calculate PV potential."""
    c1, c2, c3, c4, beta = 4.3, 0.943, 0.028, -1.528, -0.005
    T_cell = c1 + c2 * (ds.t2m - 273.15) + c3 * ds.ssrd / 3600 + c4 * ds.wspd
    perf = 1 + beta * (T_cell - 25)
    pv_pot = perf * ds.ssrd / 3600 / 1000  # kWh/m²
    pv_pot.attrs["units"] = "kWh/m²"
    return pv_pot