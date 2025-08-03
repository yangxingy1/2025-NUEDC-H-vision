import os

# 设置你的目标文件夹路径
folder_path = r"C:\Users\asus\Desktop\image"

# 获取所有文件（忽略子文件夹）
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
files.sort()  # 可选：按原始文件名排序

# 遍历并重命名
for i, filename in enumerate(files, start=309):
    name, ext = os.path.splitext(filename)  # 分离名称与扩展名
    new_name = f"{i:03d}{ext}"  # 生成如 001.jpg、002.png 等
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"重命名: {filename} -> {new_name}")

print("✅ 全部文件已重命名完成！")
