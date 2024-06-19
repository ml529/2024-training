# 提示用户输入名字
name = input("请输入您的名字: ")

# 将名字写入 guest.txt 文件
with open('guest.txt', 'a') as file:
    file.write(f"{name}\n")

print(f"{name} 已添加到访客簿。")
