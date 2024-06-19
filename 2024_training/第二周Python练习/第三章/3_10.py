# -*- coding: utf-8 -*-

# 创建一个包含山川、河流、国家、城市、语言等的列表
places_and_things = ["Mount Everest", "Amazon River", "China", "New York City", "Spanish"]

# 使用本章介绍的所有函数来处理这个列表
print("\nOriginal list:", places_and_things)

# 使用 append() 添加一个元素
places_and_things.append("Python")
print("After append:", places_and_things)

# 使用 remove() 删除一个元素
places_and_things.remove("Amazon River")
print("After remove:", places_and_things)

# 使用 reverse() 反转列表
places_and_things.reverse()
print("After reverse:", places_and_things)

# 使用 sort() 对列表进行排序
places_and_things.sort()
print("After sort:", places_and_things)
