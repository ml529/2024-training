
# 创建一个包含5种简单食品的元组
food_tuple = ("noodles", "rice", "soup", "dumplings", "vegetables")

# 使用for循环打印元组中的食品
print("\nThe original menu at the buffet:")
for food in food_tuple:
    print(food)

# 尝试修改元组中的一个元素，核实Python会拒绝这样做
# 修改元组中的一个元素会导致TypeError
try:
    food_tuple[0] = "spaghetti"
except TypeError:
    print("\nYou cannot modify a tuple once it is created.")

# 餐馆调整菜单，替换了两种食品
# 创建一个新的元组来表示新的菜单
new_food_tuple = ("noodles", "rice", "sandwich", "dumplings", "salad")

# 使用for循环打印新元组中的食品
print("\nThe new menu at the buffet:")
for food in new_food_tuple:
    print(food)
