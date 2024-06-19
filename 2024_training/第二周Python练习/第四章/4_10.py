# -*- coding: utf-8 -*-

pizza_list = ['Pepperoni', 'Margherita', 'Vegetarian', 'Hawaiian', 'California']

# 打印消息并使用切片打印列表的前三个元素
print("The first three items in the list are:")
for item in pizza_list[:3]:
    print(item)

# 打印消息并使用切片打印列表中间的三个元素
print("\nThree items from the middle of the list are:")
middle_index = len(pizza_list) // 2
for item in pizza_list[middle_index - 1:middle_index + 2]:
    print(item)

# 打印消息并使用切片打印列表末尾的三个元素
print("\nThe last three items in the list are:")
for item in pizza_list[-3:]:
    print(item)


