# 练习 8.3：T恤

def make_shirt(size, message):
    print(f"Make a {size} T-shirt with the message '{message}' on it.")

# 使用位置实参调用函数
make_shirt('Large', "I love Python")

# 使用关键字实参调用函数
make_shirt(size='Medium', message="I love Python")
