# 读取文件，替换 "Python" 为 "C"，并打印修改后的内容
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.replace('Python', 'C').strip())
