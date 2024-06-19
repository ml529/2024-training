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

# 打印用户信息摘要
def print_user_info(user_info):
    print(f"用户名: {user_info.get('username', '未知')}")
    print(f"电子邮件地址: {user_info.get('email', '未知')}")
    print(f"年龄: {user_info.get('age', '未知')}")

# 运行程序
user_info = get_user_info()
store_user_info(user_info)
print_user_info(user_info)
