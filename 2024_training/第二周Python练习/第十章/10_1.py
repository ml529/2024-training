# 读取整个文件并打印
with open('learning_python.txt', 'r') as file:
    contents = file.read()
    print(contents)

# 将所有行存储在一个列表中，然后遍历列表中的各行
with open('learning_python.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
