# 练习 6.8：宠物

pets = [
    {
        'type': 'dog',
        'owner': 'John'
    },
    {
        'type': 'cat',
        'owner': 'Jane'
    },
    {
        'type': 'bird',
        'owner': 'Edward'
    }
]

# 遍历列表并打印每只宠物的信息
for pet in pets:
    for key, value in pet.items():
        print(f"{key}: {value}")
    print("")  # 打印一个空行作为分隔
