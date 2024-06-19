# 练习 8.13：用户简介

def build_profile(first_name, last_name, **user_info):
    profile = {}
    profile['name'] = first_name + ' ' + last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

# 调用函数创建有关你的简介
user_profile = build_profile('John', 'Doe', age=30, location='New York', job='Engineer')
print(user_profile)
