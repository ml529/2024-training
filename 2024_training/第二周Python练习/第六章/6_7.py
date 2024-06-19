# 练习 6.7：人们

person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 25,
    'city': 'Los Angeles'
}

people = [person1, person2]

# 遍历列表并打印每个人的信息
for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("")  # 打印一个空行作为分隔
