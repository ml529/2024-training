# 练习 7.9：五香烟熏牛肉卖完了

sandwich_orders = ['tuna', 'ham', 'veggie', 'chicken', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

# 打印五香烟熏牛肉卖完了的消息
print("I'm sorry, but the pastrami is sold out.")

# 使用while循环删除列表中的'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 制作剩下的三明治
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches are ready!")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
