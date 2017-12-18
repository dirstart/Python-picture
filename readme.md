### 数字图像处理课程设计---验证码识别

#### 继一年之后再入Python，选修四门课，三门课用Python
#### learning文件夹下为学习的过程，practice为正式的编程（应付课程设计）的过程
#### 需要安装的东西有：
1.python
2.python的IDE，我用sublime，不推荐原生的IDLE
3.需要用到的库，numpy，Pillow（PIL）

### 坑

#### 1.第一坑 (unicode error) 'unicodeescape' codec can't decode bytes in positi
> 解决方案：\v可以作为转义字符，表示纵向制表符，这里你把后斜杠全部改为前斜杠试试。建议以后凡是路径名中的\，全部改为\\或者/，以避免转义字符的歧义。