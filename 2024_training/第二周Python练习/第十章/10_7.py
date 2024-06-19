# 提示用户输入两个数并相加，允许用户在错误后继续输入
while True:
    try:
        num1 = input("请输入第一个数: ")
        num2 = input("请输入第二个数: ")
        
        # 转换为整数
        num1 = int(num1)
        num2 = int(num2)
        
        # 相加并打印结果
        result = num1 + num2
        print(f"结果是: {result}")
        break  # 跳出循环
    except ValueError:
        print("请输入有效的整数。")
