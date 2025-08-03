import os
import json
from glob import glob

# 类别映射表
label_map = {
    "tiger": 0,
    "elephant": 1,
    "monkey": 2,
    "wolf": 3,
    "peacock": 4
}

def convert_to_yolo(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    image_width = data['imageWidth']
    image_height = data['imageHeight']
    shapes = data['shapes']

    yolo_labels = []
    for shape in shapes:
        label = shape['label']
        if label not in label_map:
            print(f"跳过未知类别: {label}")
            continue
        class_id = label_map[label]
        points = shape['points']

        # 获取边界框坐标
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        xmin, xmax = min(x_coords), max(x_coords)
        ymin, ymax = min(y_coords), max(y_coords)

        # 转换为 YOLO 格式 (cx, cy, w, h)，并归一化
        cx = (xmin + xmax) / 2.0 / image_width
        cy = (ymin + ymax) / 2.0 / image_height
        w = (xmax - xmin) / image_width
        h = (ymax - ymin) / image_height

        yolo_labels.append(f"{class_id} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}")

    # 写入 YOLO 格式 .txt 文件
    txt_path = os.path.splitext(json_path)[0] + ".txt"
    with open(txt_path, 'w') as f:
        f.write("\n".join(yolo_labels))
    print(f"✔ 转换完成: {os.path.basename(json_path)}")

def batch_convert(folder_path):
    json_files = glob(os.path.join(folder_path, "*.json"))
    for json_file in json_files:
        convert_to_yolo(json_file)

# 使用示例
folder_path = r"C:\Users\asus\Desktop\image" # ← 改成你的路径
batch_convert(folder_path)
