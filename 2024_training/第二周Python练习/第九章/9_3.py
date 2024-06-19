from user import User
# 创建多个用户实例
user1 = User('张', '三', 30, '北京')
user2 = User('李', '四', 25, '上海')
user3 = User('王', '五', 22, '广州')

# 对每个实例调用 describe_user() 和 greet_user() 方法
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
