from PIL import Image  
from numpy import *  
from pylab import *  
from matplotlib import pyplot  
#from scipy.misc import *  
from scipy.misc import toimage  

# 定义直方图均衡化函数，这里传入的参数是灰度图像的数组和累积分布函数值  
def histImageArr(im_arr, cdf):  
    cdf_min = cdf[0]  
    im_w = len(im_arr[0])  
    im_h = len(im_arr)  
    im_num = im_w*im_h  
    color_list = []  
    i=0  
  
    # 通过累积分布函数计算灰度转换值  
    while i<256:  
        if i>len(cdf) - 1:  
            color_list.append(color_list[i-1])  
            break  
        tmp_v = (cdf[i] - cdf_min)*255/(im_num-cdf_min)  
        color_list.append(tmp_v)  
        i += 1  
  
    # 产生均衡化后的图像数据  
    arr_im_hist = []  
    for itemL in im_arr:  
        tmp_line = []  
        for item_p in itemL:  
            tmp_line.append(color_list[item_p])  
        arr_im_hist.append(tmp_line)  
  
    return arr_im_hist  
  
# 封装一下图像处理的函数,cdf是累积分布函数数值  
def beautyImage(im_arr):  
    imhist, bins = histogram(im_arr.flatten(), range(256))  
    cdf = imhist.cumsum()  
  
    return histImageArr(im_arr, cdf)  
  
  
im_source = Image.open('1.jpg')  
  
if True:  
    im_source.show()  
  
if True:  
    # 灰度图像的转换  
    im_gray = im_source.convert('L')  
    im_gray.show()  
  
    arr_im_gray = array(im_gray)  
    arr_im_gray_hist = beautyImage(arr_im_gray)  
    figure()  
    im_conver = toimage(arr_im_gray_hist, 255, 0, None, None, None, 'L')  
    im_conver.show()  
  
figure()  
im_beauty = toimage(array(arr_im_hist), 255)
im_beauty.show()