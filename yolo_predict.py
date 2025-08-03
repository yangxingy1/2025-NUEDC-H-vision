import os
from ultralytics import YOLO

# 模型路径
model_path = 'last.pt'

# 待预测图片所在文件夹
source_folder = r"testfile"

# 输出文件夹（预测结果保存在此）
output_folder = 'result'

# 加载模型
model = YOLO(model_path)

# 执行预测
results = model.predict(
    source=source_folder,
    save=True,
    project='result',
    name='predict_results',
    imgsz=320
)

result = ["tiger", "elephant", "monkey", "wolf", "peacock"]
