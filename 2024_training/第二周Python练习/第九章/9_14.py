import random
# 创建一个包含10个数字和5个字母的列表
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 随机选择4个元素
winning_numbers = random.sample(lottery_pool, 4)

# 打印中奖消息
print(f"只要彩票上是这4个数字或字母，就中大奖了: {winning_numbers}")
