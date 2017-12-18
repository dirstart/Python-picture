# 引入要使用的库
import numpy as np
from PIL import Image
# 利用PIL打开图片
im = Image.open('F:/xx.ico');
# 将图片另存为
im.save('newXX.ico');
im.save('F:/test.ico');
# 将图片打开
# im.show()
# 将PIL image图片转换为 numpy 数组
im_array = np.array(im)
# 将图片转换为灰度图
gray = im.convert('L');
# gray.show();
print(im_array)