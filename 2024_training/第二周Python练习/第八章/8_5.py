# 练习 8.5：城市

def describe_city(city, country=None):
    if country:
        print(f"{city} is in {country}.")
    else:
        print(f"{city} is in Iceland.")

# 调用函数描述不同城市
describe_city("Reykjavik")  # Reykjavik默认在Iceland
describe_city("New York", "USA")  # New York不在Iceland
describe_city("Paris")  # Paris默认在Iceland
