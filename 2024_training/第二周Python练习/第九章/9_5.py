from user import User
# 创建实例
user = User('张', '三', 30, '北京')

# 调用 increment_login_attempts() 方法多次
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# 打印 login_attempts 的值
print(f"登录尝试次数: {user.login_attempts}")

# 调用 reset_login_attempts() 方法
user.reset_login_attempts()

# 再次打印 login_attempts 的值
print(f"登录尝试次数: {user.login_attempts}")
