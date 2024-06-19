# 直接遍历 readlines() 返回的列表
with open('learning_python.txt', 'r') as file:
    for line in file.readlines():
        print(line.strip())
