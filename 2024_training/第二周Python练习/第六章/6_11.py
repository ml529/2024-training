# 练习 6.11：城市

cities = {
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'The city that never sleeps'
    },
    'London': {
        'country': 'UK',
        'population': '8.8 million',
        'fact': 'The capital of England'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '37.8 million',
        'fact': 'The largest city in the world by population'
    }
}

# 遍历字典并打印每座城市的信息
for city, details in cities.items():
    print(f"{city}")
    for key, value in details.items():
        print(f"- {key}: {value}")
    print("")  # 打印一个空行作为分隔
