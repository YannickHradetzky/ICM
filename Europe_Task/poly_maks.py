import numpy as np
import xarray as xr
from shapely.geometry import Polygon, Point

def create_polygon_mask(dataset, coordinates, longitude_dim='longitude', latitude_dim='latitude'):
    """
    Create a boolean mask for an xarray dataset based on a set of polygon coordinates.
    
    Parameters:
    -----------
    dataset : xarray.Dataset or xarray.DataArray
        The input dataset to be masked
    coordinates : list of tuples
        List of (longitude, latitude) coordinates defining the polygon boundary.
        Coordinates should be ordered to form a complete boundary, for example:
        [(west, north), (east, north), (east, south), (west, south), (west, north)]
        Note: The last point should match the first point to close the polygon.
    longitude_dim : str, optional
        Name of the longitude dimension (default: 'longitude')
    latitude_dim : str, optional
        Name of the latitude dimension (default: 'latitude')
    
    Returns:
    --------
    xarray.DataArray
        A boolean mask with the same shape as the input dataset's spatial dimensions
    """
    # Create a Shapely polygon from the given coordinates
    polygon = Polygon(coordinates)
    
    # Extract longitude and latitude coordinates
    lons = dataset[longitude_dim].values
    lats = dataset[latitude_dim].values
    
    # Create a meshgrid of all coordinate combinations
    lon_grid, lat_grid = np.meshgrid(lons, lats)
    
    # Create a mask using Shapely's contains method
    mask = np.zeros_like(lon_grid, dtype=bool)
    
    for i in range(lon_grid.shape[0]):
        for j in range(lon_grid.shape[1]):
            point = Point(lon_grid[i, j], lat_grid[i, j])
            mask[i, j] = polygon.contains(point)
    
    # Convert to xarray DataArray with the same coordinates
    mask_da = xr.DataArray(
        mask, 
        coords={latitude_dim: dataset[latitude_dim], 
                longitude_dim: dataset[longitude_dim]},
        dims=[latitude_dim, longitude_dim]
    )
    
    return mask_da

# Example usage
def apply_polygon_mask(dataset, coordinates, longitude_dim='longitude', latitude_dim='latitude'):
    """
    Apply the polygon mask to the entire dataset.
    
    Parameters:
    -----------
    dataset : xarray.Dataset or xarray.DataArray
        The input dataset to be masked
    coordinates : list of tuples
        List of (longitude, latitude) coordinates defining the polygon boundary
    longitude_dim : str, optional
        Name of the longitude dimension (default: 'longitude')
    latitude_dim : str, optional
        Name of the latitude dimension (default: 'latitude')
    
    Returns:
    --------
    xarray.Dataset or xarray.DataArray
        Masked dataset with values outside the polygon set to NaN
    """
    # Create the mask
    mask = create_polygon_mask(dataset, coordinates, longitude_dim, latitude_dim)
    
    # Apply mask to the dataset
    return dataset.where(mask)