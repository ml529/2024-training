# -*- coding: utf-8 -*-

destinations = ["New York", "Sydney", "Tokyo", "Rome", "Cairo"]

# 按原始排列顺序打印该列表
print("Original order:", destinations)

# 使用 sorted() 按字母顺序打印这个列表
print("Sorted order:", sorted(destinations))

# 再次打印该列表，核实排列顺序未变
print("Original order after sorted:", destinations)

# 使用 sorted() 按与字母顺序相反的顺序打印这个列表
print("Reverse sorted order:", sorted(destinations, reverse=True))

# 再次打印该列表，核实排列顺序未变
print("Original order after reverse sorted:", destinations)

# 使用 reverse() 修改列表元素的排列顺序
destinations.reverse()
print("Reversed order:", destinations)

# 使用 reverse() 再次修改列表元素的排列顺序
destinations.reverse()
print("Original order after reversing:", destinations)

# 使用 sort() 修改该列表，使其元素按字母顺序排列
destinations.sort()
print("Sorted order using sort():", destinations)

# 使用 sort() 修改该列表，使其元素按与字母顺序相反的顺序排列
destinations.sort(reverse=True)
print("Reverse sorted order using sort():", destinations)




