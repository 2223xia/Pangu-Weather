import numpy as np
import os
import matplotlib.pyplot as plt


output_data_dir = 'output_data'
# Load the upper-air numpy arrays
upper = np.load(os.path.join(output_data_dir, 'output_upper.npy')).astype(np.float32)
# Load the surface numpy arrays
surface = np.load(os.path.join(output_data_dir, 'output_surface.npy')).astype(np.float32)
print(upper.shape)
print(surface.shape)
# 输出查看surface第1维所有数据
print(surface[3])
# 绘制surface第1维平面的数据
plt.imshow(surface[3])
plt.show()