# 🏀 Basketball Player Detection  

Real-time **object detection system** to identify and track basketball players in video streams.  
This project is a foundation for **advanced sports analytics**, leveraging deep learning to achieve **lightweight, fast, and accurate** detection.  

---

## 🎯 Project Goal  
To develop a **real-time basketball player detection system** that balances **accuracy** and **speed**, making it suitable for live sports analytics applications.  

---

## 📌 Objectives  
- Detect and track basketball players in real-time.  
- Build a **lightweight yet accurate** object detection pipeline.  
- Lay the groundwork for future sports analytics (heatmaps, movement analysis, performance tracking).  

---

## ⚙️ Technical Methodology & Tools  

### 🧠 Core Technology  
- **YOLOv5 (Ultralytics)**  
- Benchmarked against **YOLOv8** and **YOLOv11** with varying epochs.  
- YOLOv5 provided the **best trade-off** between **speed (FPS)** and **accuracy (mAP)**, making it ideal for real-time inference.  

### 🛠️ Tools Used  
- **Google Colab GPU** – Model training  
- **Roboflow** – Dataset preparation and augmentation  
- **Ultralytics YOLO** – Training & inference  
- **OpenCV** – Video stream processing  

---

## 🔄 Workflow  

### Flowchart  
<img width="600" alt="Flowchart" src="https://github.com/user-attachments/assets/db7506f8-2ff2-4f7d-aadb-d5977bfe8fe6" />  

---

## 📊 Model Training  

- Dataset prepared with **Roboflow**.  
- Trained on **Google Colab (GPU)**.  
- Generated optimized weights (`best.pt`).  
- Evaluated across different YOLO versions & epochs for performance.  

<img width="500" alt="training" src="https://github.com/user-attachments/assets/69003781-047f-4519-9524-8a4815b0f546" />  

<img width="1700" alt="graph" src="https://github.com/user-attachments/assets/130173a5-7888-4d4d-a230-7ed619775514" />  

---

## ✅ Results  

- Successfully achieved **real-time detection** with smooth tracking.  
- Optimized YOLOv5 weights used for final inference.  

<img width="400" alt="result1" src="https://github.com/user-attachments/assets/d47a3eed-b0e7-4cb5-a7b5-4a2771abd4f7" />  

<img width="1700" alt="result2" src="https://github.com/user-attachments/assets/a4962198-f2c6-4fe6-bb66-2e367e778b74" />  

<img width="450" alt="result3" src="https://github.com/user-attachments/assets/59f0f4b8-588a-46f5-9c37-740dd63fde22" />  

<img width="460" alt="result4" src="https://github.com/user-attachments/assets/b70e2ac7-2180-4e58-9069-257234d31058" />  

---

## 📌 Future Scope  
- Player movement heatmaps.  
- Individual performance metrics.  
- Integration with **sports analytics dashboards**.  

---

## 🚀 How to Run  

1. Clone the repo  
   ```bash
   git clone https://github.com/Dhananjay4yu/Basketball_Player_Tracker.git
   cd Basketball_Player_Tracker
