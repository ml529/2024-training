

# 假设我们有两个比萨列表
my_pizzas = ['Pepperoni', 'Margherita', 'Vegetarian']
friend_pizzas = my_pizzas.copy()  # 创建一个副本

# 在原来的比萨列表中添加一种比萨
my_pizzas.append('Hawaiian')

# 在列表 friend_pizzas 中添加另一种比萨
friend_pizzas.append('California')

# 核实有两个不同的列表
print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
