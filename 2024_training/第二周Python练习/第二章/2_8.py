# -*- coding: utf-8 -*-

# 练习 2.8：文件扩展名
# 将值 'python_notes.txt' 赋给变量 filename
filename = 'python_notes.txt'

# 使用 removesuffix() 方法来显示不包含扩展名的文件名
#filename_without_suffix = filename.removesuffix('.txt')

#print(filename_without_suffix)

# 使用切片操作来移除扩展名

# 找到最后一个点号的位置
dot_index = filename.rfind('.')

# 如果找到了点号，就切片移除点号之后的所有字符
if dot_index != -1:
    filename_without_suffix = filename[:dot_index]
else:
    filename_without_suffix = filename

print(filename_without_suffix)
