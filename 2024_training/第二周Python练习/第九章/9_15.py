import random
# 创建一个名为 my_ticket 的列表
my_ticket = [1, 2, 3, 4]
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
# 编写一个循环，不断地随机选择元素，直到中大奖为止
attempts = 0
while True:
    attempts += 1
    random_ticket = random.sample(lottery_pool, 4)
    if random_ticket == my_ticket:
        break

# 打印中了大奖所需的循环次数
print(f"执行了 {attempts} 次循环才中了大奖。")
