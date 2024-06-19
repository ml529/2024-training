# 练习 6.9：喜欢的地点

favorite_places = {
    'John': ['New York', 'Las Vegas'],
    'Jane': ['Paris', 'London'],
    'Edward': ['Tokyo', 'Sydney']
}

# 遍历字典并打印每个人的名字及其喜欢的地点
for name, places in favorite_places.items():
    print(f"{name}'s favorite places:")
    for place in places:
        print(f"- {place}")
    print("")  # 打印一个空行作为分隔
