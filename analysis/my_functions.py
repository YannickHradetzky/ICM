import numpy as np
import xarray as xr
import time


def calc_ws(ds):
    return np.sqrt(np.power(ds["u10"], 2)+np.power(ds["v10"], 2))


def calc_pv_pot(ds):
    c1 = 4.3
    c2 = 0.943
    c3 = 0.028
    c4 = -1.528
    beta = -0.005

    T_cell = c1 + c2 * (ds.t2m - 273.15) + c3 * ds.ssrd/3600 + c4 * ds.wspd

    perf = 1 + beta*(T_cell-25)

    pv_pot = perf * ds.ssrd/3600 * 1/1000
    return pv_pot


def calculate_mean_year(year:str, path = "/home/yannickh00/LEHRE/msc-intro-comp-met-ex-w2024/data/era5/"):
    ds=xr.open_mfdataset(path+"era5-{year}-*.nc", engine="netcdf4", chunks={"valid_time":1e5} )
    ds["wspd"] = calc_ws(ds)
    pvpot = calc_pv_pot(ds).groupby(ds.valid_time.dt.month).mean("valid_time").compute()
    return pvpot, ds
