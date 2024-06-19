# 创建 cats.txt 和 dogs.txt 文件，并写入一些名字
with open('cats.txt', 'w') as file:
    file.write("猫1\n猫2\n猫3\n")

with open('dogs.txt', 'w') as file:
    file.write("狗1\n狗2\n狗3\n")

# 读取 cats.txt 文件
try:
    with open('cats.txt', 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line.strip())
except FileNotFoundError:
    print("抱歉，文件 cats.txt 未找到。")

# 读取 dogs.txt 文件
try:
    with open('dogs.txt', 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line.strip())
except FileNotFoundError:
    print("抱歉，文件 dogs.txt 未找到。")
