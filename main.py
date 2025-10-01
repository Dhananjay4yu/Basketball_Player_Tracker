from ultralytics import YOLO

model = YOLO("models/best.pt")

results = model.predict("input_videos/video_3.mp4", save=True, stream=True)

for result in results:
    for box in result.boxes:
        print(box)
