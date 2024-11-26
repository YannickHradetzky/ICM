from dask.distributed import Client, LocalCluster
import xarray as xr
import numpy as np
import time
import core as c
import poly_maks as pm
import glob
import argparse

def main(year, client):
    path_local = "/Users/yhra/Documents/Master/Semester_3/ICM/Europe_Task/offline_data/"
    wdir_local = "/Users/yhra/Documents/Master/Semester_3/ICM/Europe_Task/"
    path="/home/yannickh00/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"
    wdir = "/home/yannickh00/ICM/Europe_Task/"

    boundaries = [
                (70.829421, -11.212043),
                (71.356409, 39.071939),
                (37.287328, 44.764466),
                (35.762589, -13.516161)
                ]
    
    # load the data
    all_files = glob.glob(path_local + "*")[0]
    print(all_files)
    ds=xr.open_dataset(all_files, engine="netcdf4", chunks={"valid_time":1e5} )
    ds = pm.apply_polygon_mask(ds, boundaries)

    # calculate the windspeed
    ds["wspd"] = c.calc_windspeed(ds)
    # calculate the pv potential and group it by months
    print("Calculating pv mean")
    pvpot = c.calc_pv_pot(ds).groupby(ds.valid_time.dt.month).mean("valid_time").compute()
    client.shutdown()
    # save the results
    pvpot.to_netcdf(wdir_local + f"Results/coarse/pvpot_{year}.nc")
    return pvpot

if __name__ == "__main__":
    
    start = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=str, help="year to compute the mean for")
    args = parser.parse_args()
    
    client = Client(n_workers=1, threads_per_worker=1, local_directory='~/tmp')
    main(args.year, client)
    end = time.time()
    print(f"Program took {end-start:.4f} seconds")