# 练习 6.5：河流

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# 打印每条河流的信息
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# 打印河流的名字
for river in rivers:
    print(river)

# 打印流经的国家
for country in rivers.values():
    print(country)
