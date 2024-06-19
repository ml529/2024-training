# 练习 5.9：处理没有用户的情况

usernames = []  # 删除所有用户名，使列表为空

if not usernames:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
