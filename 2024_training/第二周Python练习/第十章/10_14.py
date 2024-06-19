import json

# 获取用户信息
def get_user_info():
    username = input("请输入你的用户名: ")
    email = input("请输入你的电子邮件地址: ")
    age = input("请输入你的年龄: ")
    return {
        'username': username,
        'email': email,
        'age': age
    }
# 获取新的用户名
def get_new_username():
    username = input("请输入你的新用户名: ")
    return username

# 将用户信息存储到文件中
def store_user_info(user_info):
    with open('user_info.json', 'w') as file:
        json.dump(user_info, file)

# 从文件中读取用户信息
def read_user_info():
    try:
        with open('user_info.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# 验证用户名
def verify_username(user_info):
    username = input("请输入你的用户名: ")
    if username == user_info.get('username', '未知'):
        return True
    else:
        return False

# 问候用户
def greet_user(user_info):
    if verify_username(user_info):
        print(f"欢迎回来，{user_info['username']}！")
    else:
        user_info['username'] = get_new_username()
        store_user_info(user_info)
        print(f"你好，{user_info['username']}！这是你的第一次访问吗？")

# 运行程序
user_info = read_user_info()
greet_user(user_info)
