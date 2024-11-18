import xarray as xr
import glob
import core as c
import os
import argparse
from dask.distributed import Client
import time

def main(year, client):
    path="/Users/yhra/Documents/Master/Semester_3/ICM/offline_data/"
    wdir = "/Users/yhra/Documents/Master/Semester_3/ICM/Europe_Task"
    all_files = glob.glob(path+"*")
    all_files = [f for f in all_files if f"{year}" in f]
    print(f"Importing {len(all_files)} files")
    for f in all_files:
        print(f + "\n")
    ds=xr.open_mfdataset(all_files, engine="netcdf4", chunks={"valid_time":1e5} )
    ds = c.clip_to_europe(ds, shapefile_path=wdir+"/europe_10km.shx")
    ds["wspd"] = c.calc_windspeed(ds)
    pvpot = c.calc_pv_pot(ds).groupby(ds.valid_time.dt.month).mean("valid_time").compute()
    
    if not os.path.exists(wdir+"/Results"): # check if the directory exists
        os.makedirs(wdir+"/Results") 
    pvpot.to_netcdf(wdir+f"/Results/pvpot_{year}.nc") # save as .nc file
    client.shutdown()
    return pvpot

if __name__ == "__main__":
    start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=str, help="year to compute the mean for")
    args = parser.parse_args()
    
    # Create a client
    client = Client(n_workers=5, threads_per_worker=1, local_directory='/tmp')

    # Call the main function with the provided path
    mean_data = main(args.year, client)
    end = time.time()
    print(f"Program took {end-start:.4f} seconds")
