import os

# 文件夹路径
folder_path = "E:\\study\\xiaomi-training\\2024_training\\Python练习\\第五章"

# 创建从4_1.py到4_10.py的文件
for x in range(1, 11):
    # 构建文件名
    file_path = os.path.join(folder_path, f"5_{x}.py")
    
    # 创建文件
    with open(file_path, "w"):
        pass

print("所有文件已创建完成。")