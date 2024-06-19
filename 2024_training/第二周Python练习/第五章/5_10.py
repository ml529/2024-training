# 练习 5.10：检查用户名

current_users = ['John', 'Mary', 'Lucy', 'Tom', 'Emma']
new_users = ['John', 'MARY', 'Lucy', 'Mike', 'emma']

# 创建当前用户名的全小写版本
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username {new_user} is already taken. Please enter a different username.")
    else:
        print(f"The username {new_user} is available.")
