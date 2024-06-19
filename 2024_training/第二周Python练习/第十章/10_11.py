import json

# 提示用户输入喜欢的数
favorite_number = input("请输入你喜欢的数: ")

# 使用 json.dumps() 将喜欢的数存储在文件中
with open('favorite_number.json', 'w') as file:
    json.dump(favorite_number, file)

print(f"已将你喜欢的数 {favorite_number} 存储在文件中。")
