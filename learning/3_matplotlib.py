# plt用于显示图片
import matplotlib.pyplot as plt
# mping用于读取图片
import matplotlib.image as mping
import numpy as np

pic = mping.imread('xx.ico');
# 此时pic为一个 np.array ，可以对它进行任意处理
pic.shape
# 显示图片
plt.imshow(pic)
# 不显示坐标
# plt.axis('off')
plt.show()

