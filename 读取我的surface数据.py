import xarray as xr
import numpy as np

# 读取数据，变量顺序为msl、u10、v10、t2m
my_surface = xr.open_dataset('./my_data/adaptor.mars.internal-1690442150.0414987-6212-5-47d79789-8911-4c39-8525-4fcabac58609.nc')
my_upper = xr.open_dataset('./my_data/adaptor.mars.internal-1690440283.3816683-22512-12-e306c64b-aa26-478f-9ca2-865d199cf941.nc')

# 将数据的var按指定顺序排列
my_surface = my_surface[['msl', 'u10', 'v10', 't2m']]
# 将my_upper的z数值乘以9.80665
my_upper['z'] = my_upper['z'] * 9.80665

# 将数据转换为numpy数组
surface_data = my_surface.to_array().values
upper_data = my_upper.to_array().values
# 去掉surface和upper的第2维
surface_data = surface_data[:, 0, :, :]
upper_data = upper_data[:, 0, :, :]

# 保存数据为npy文件
np.save('./my_data/input_surface', surface_data)
np.save('./my_data/input_upper', upper_data)


