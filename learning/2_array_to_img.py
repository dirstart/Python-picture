# 引入要使用的库
import numpy as np
import matplotlib.image as mping
from PIL import Image

lena = mping.imread('F:/xx.ico');
im = Image.open('F:/xx.ico');
nptest = np.array(im);

