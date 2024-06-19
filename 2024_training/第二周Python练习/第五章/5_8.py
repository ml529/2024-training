# 练习 5.8：以特殊方式跟管理员打招呼

usernames = ['admin', 'Jaden', 'Ethan', 'Lucy', 'Emma']

for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")
