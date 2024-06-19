# 练习 8.4：大号T恤

def make_shirt(size='Large', message="I love Python"):
    print(f"Make a {size} T-shirt with the message '{message}' on it.")

# 调用函数制作不同尺码和字样的T恤
make_shirt()  # 默认大号T恤，印有“I love Python”
make_shirt(size='Medium')  # 中号T恤，印有默认字样
make_shirt(message="Python is fun")  # 大号T恤，印有其他字样
