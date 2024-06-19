# -*- coding: utf-8 -*-
from restaurant import Restaurant
# 创建实例
restaurant = Restaurant('大福来', '天津菜')

# 打印属性
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# 调用方法
restaurant.describe_restaurant()
restaurant.open_restaurant()