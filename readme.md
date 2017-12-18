#### 继一年之后再入Python，选修四门课，三门课用Python

### 坑

#### 1.第一坑 (unicode error) 'unicodeescape' codec can't decode bytes in positi
> 解决方案：\v可以作为转义字符，表示纵向制表符，这里你把后斜杠全部改为前斜杠试试。建议以后凡是路径名中的\，全部改为\\或者/，以避免转义字符的歧义。