import json

# 检查文件中是否存储了喜欢的数
def read_favorite_number():
    try:
        with open('favorite_number.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# 提示用户输入喜欢的数
def get_favorite_number():
    favorite_number = input("请输入你喜欢的数: ")
    return favorite_number

# 显示喜欢的数或提示用户输入
def show_or_get_favorite_number():
    favorite_number = read_favorite_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_favorite_number()
        with open('favorite_number.json', 'w') as file:
            json.dump(favorite_number, file)
        print(f"已将你喜欢的数 {favorite_number} 存储在文件中。")

# 运行程序两次
show_or_get_favorite_number()
show_or_get_favorite_number()
