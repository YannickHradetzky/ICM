import numpy as np
import xarray as xr
import time

def windspeed(_ds):
    return np.sqrt(np.power(_ds["u10"],2)+np.power(_ds["v10"],2))

def windspeed2(a, b):
    func = lambda x, y: np.sqrt(x**2 + y**2)
    return xr.apply_ufunc(func, a, b, dask="parallelized")

def pv_pot(_ds):

    sechour=3600 # seconds per hour
    c1 = 4.3
    c2 = 0.943
    c3 = 0.028
    c4 = -1.528

    # cell temperature
    T_cell = c1 + c2 * (_ds.t2m - 273.15) + c3 * _ds.ssrd/sechour + c4 * _ds.wspd

    # performance ratio
    beta = -0.005
    p_r = 1 + beta*(T_cell-25)

    # pv potential
    pv_pot = p_r * _ds.ssrd/(sechour) * 1/1000

    return pv_pot


def measure_performance(code_to_run):
    start_time = time.time()
    # Run the code
    code_to_run()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.5f} seconds")