from ultralytics import YOLO

def main():
    model = YOLO('yolo11n.pt')

    # 训练模型
    model.train(
        data='coco.yaml',
        epochs=200,
        imgsz=320,
        batch=16,
        name='yolo_custom',
        device=0
    )


if __name__ == '__main__':
    main()
