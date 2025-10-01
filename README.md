# 🏀 Basketball Player Detection  

Real-time **object detection system** to identify and track basketball players in video streams.  
This project is a foundation for **advanced sports analytics**, leveraging deep learning to achieve **lightweight, fast, and accurate** detection.  

---

## Project Goal  
To develop a **real-time basketball player detection system** that balances **accuracy** and **speed**, making it suitable for live sports analytics applications.  

---

##  Objectives  
-  Detect and track basketball players in real-time  
-  Build a **lightweight yet accurate** object detection pipeline  
-  Lay the groundwork for **future sports analytics** (heatmaps, movement analysis, performance tracking)  

---

## Technical Methodology & Tools  

###  Core Technology  
- **YOLOv5 (Ultralytics)**  
- Benchmarked against **YOLOv8** and **YOLOv11** with varying epochs  
- YOLOv5 provided the **best trade-off** between **speed (FPS)** and **accuracy (mAP)**, making it ideal for real-time inference  

###  Tools Used  
- **Google Colab GPU** – Model training  
- **Roboflow** – Dataset preparation and augmentation  
- **Ultralytics YOLO** – Training & inference  
- **OpenCV** – Video stream processing  

---

##  Flow Chart  

<p align="center">
  <img src="https://github.com/user-attachments/assets/c34445e5-54f5-4568-ace4-ea57d69f1dd8" alt="Flow chart" width="350"/>
</p>

---
## 🚀 How to Run  

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Dhananjay4yu/Basketball_Player_Tracker.git
   cd Basketball_Player_Tracker
