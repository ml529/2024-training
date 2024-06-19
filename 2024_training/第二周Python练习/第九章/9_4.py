# 创建实例
restaurant = Restaurant('大福来', '天津菜')

# 打印就餐人数
print(f"在这家餐馆就餐过的有: {restaurant.number_served} 人")

# 修改就餐人数并再次打印
restaurant.set_number_served(10)
print(f"在这家餐馆就餐过的有: {restaurant.number_served} 人")

# 就餐人数递增
restaurant.increment_number_served(5)
print(f"在这家餐馆就餐过的有: {restaurant.number_served} 人")