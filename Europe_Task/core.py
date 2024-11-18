import xarray as xr
import geopandas as gpd
from pathlib import Path
import warnings
import numpy as np
def clip_to_europe(ds: xr.Dataset, 
                  shapefile_path: str = None) -> xr.Dataset:
    """
    Clips an xarray Dataset to the European continent using a shapefile.
    
    Parameters:
    -----------
    ds : xr.Dataset
        The xarray Dataset to be clipped
    shapefile_path : str, optional
        Path to the Europe shapefile. If None, you need to provide your own shapefile path
        
    Returns:
    --------
    xr.Dataset
        Clipped dataset containing only data within Europe's boundaries
        
    Raises:
    -------
    FileNotFoundError
        If the shapefile doesn't exist
    ValueError
        If there are projection mismatches or other geometry issues
    """
    # Input validation
    if not isinstance(ds, xr.Dataset):
        raise ValueError("Input must be an xarray Dataset")
    
    # If shapefile_path is not provided, raise error
    if shapefile_path is None:
        raise ValueError("Please provide the path to Europe's shapefile")
    
    if not Path(shapefile_path).exists():
        raise FileNotFoundError(f"Shapefile not found: {shapefile_path}")
    
    try:
        # Load Europe shapefile
        europe_shape = gpd.read_file(shapefile_path)
        
        # Check and fix projection issues
        bounds = europe_shape.total_bounds
        if bounds[2] > 180 or bounds[1] > 90:  # If bounds are outside normal lat/lon range
            warnings.warn("Shapefile appears to be in projected coordinates. Attempting to reproject...")
            # Assume ETRS89-extended / LAEA Europe projection
            europe_shape = europe_shape.set_crs(epsg=3035, allow_override=True)
            # Reproject to EPSG:4326 (WGS84)
            europe_shape = europe_shape.to_crs(epsg=4326)
            
        # Set CRS for the dataset
        ds = ds.rio.write_crs("EPSG:4326")
        
        # Perform the clipping
        masked_data = ds.rio.clip(europe_shape.geometry, europe_shape.crs, drop=True)
        
        return masked_data
        
    except Exception as e:
        # Add context to the error
        raise type(e)(f"Error while clipping data: {str(e)}") from e
    
def calc_windspeed(ds: xr.Dataset) -> xr.Dataset:
    """
    Calculate the windspeed from u and v components
    """
    return np.sqrt(np.power(ds["u10"], 2)+np.power(ds["v10"], 2))

def calc_pv_pot(ds: xr.Dataset) -> xr.Dataset:
    """
    Calculate the pv potential from the given dataset
    """
    c1 = 4.3
    c2 = 0.943
    c3 = 0.028
    c4 = -1.528
    beta = -0.005

    T_cell = c1 + c2 * (ds.t2m - 273.15) + c3 * ds.ssrd/3600 + c4 * ds.wspd

    perf = 1 + beta*(T_cell-25)

    pv_pot = perf * ds.ssrd/3600 * 1/1000
    return pv_pot