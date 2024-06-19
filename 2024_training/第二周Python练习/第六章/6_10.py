# 练习 6.10：喜欢的数

likes = {
    'Alice': [7, 11, 13],
    'Bob': [12, 14, 15],
    'Charlie': [24, 26, 28],
    'David': [36, 38, 40],
    'Eve': [49, 51, 53]
}

# 遍历列表并打印每个人的名字及其喜欢的数
for name, numbers in likes.items():
    print(f"{name}'s favorite numbers:")
    for number in numbers:
        print(f"- {number}")
    print("")  # 打印一个空行作为分隔
