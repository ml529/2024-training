# 练习 7.8：熟食店

sandwich_orders = ['tuna', 'ham', 'veggie', 'chicken', 'pastrami']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nAll sandwiches are ready!")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
