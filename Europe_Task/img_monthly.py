import xarray as xr
import numpy as np
import time
from dask.distributed import Client, LocalCluster
import matplotlib.pyplot as plt
import glob
import argparse


def main(year, client):
    path="/home/yannickh00/ICM/Europe_Task/Results/coarse/"    
    print
    # open the dataset
    all_files = glob.glob(path + "*")
    all_files = [f for f in all_files if f"{year}" in f]
    print(f"Importing {len(all_files)} files")
    for f in all_files:
        print(f + "\n")
    ds=xr.open_mfdataset(all_files, engine="netcdf4", chunks={"valid_time":1e5} )
    return ds

def make_figure(pvpot, month, year):
    image_path = "/home/yannickh00/ICM/Europe_Task/Images/"
    pvpot = pvpot['__xarray_dataarray_variable__']
    plt.contourf(pvpot.longitude, pvpot.latitude, pvpot.sel(month=month))
    plt.colorbar()
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title(f"Mean PV-Pot for {month}-{year}")
    plt.savefig(image_path + f"{month}-{year}.png")
    plt.close()

if __name__ == "__main__":
    start = time.time()
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process ERA5 data.")
    parser.add_argument("year", type=str, help="year to compute the mean for")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Create a client
    client = Client(n_workers=20, threads_per_worker=5, local_directory='~/tmp')

    # Call the main function with the provided path
    mean_data = main(args.year, client)
    print(mean_data)

    # make a figure
    print("Making the figures")
    for month in range(1, 13):
        make_figure(mean_data, month, args.year)

    end = time.time()
    print(f"Program took {end-start:.4f} seconds")


    
    