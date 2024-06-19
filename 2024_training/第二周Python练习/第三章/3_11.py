# -*- coding: utf-8 -*-

# 引发索引错误的尝试

# 创建一个列表
sample_list = [1, 2, 3, 4, 5]

# 尝试访问一个不存在的索引，引发索引错误
try:
    print(sample_list[10])
except IndexError:
    print("IndexError encountered!")

# 修正索引，消除错误
print(sample_list[4])
