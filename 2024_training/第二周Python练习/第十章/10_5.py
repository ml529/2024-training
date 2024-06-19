# 打开 guest_book.txt 文件进行写入
with open('guest_book.txt', 'w') as file:
    while True:
        # 提示用户输入名字
        name = input("请输入您的名字 (输入 'done' 结束): ")
        if name.lower() == 'done':
            break
        # 将名字写入文件
        file.write(f"{name}\n")

print("访客簿已更新。")
