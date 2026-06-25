# 🔥 IOCL Fire & Smoke Detection System

## 🌐 Live Demo

**Streamlit Dashboard:**  
https://fireandsmokedetec.streamlit.app/

**GitHub Repository:**  
https://github.com/mandrita16/IOCL-Fire-and-Smoke-Detection

---

# 📖 Project Overview

The IOCL Fire & Smoke Detection System is an AI-powered industrial safety monitoring solution developed using YOLOv8, OpenCV, and Streamlit.

The system continuously monitors CCTV footage and automatically detects:

- 🔥 Fire
- 💨 Smoke

Whenever a fire or smoke incident is detected, the system:

- Captures evidence screenshots
- Logs detection details
- Triggers an alarm
- Displays incidents on a live dashboard
- Maintains historical records for analysis

The project is designed for industrial environments such as oil refineries, chemical plants, warehouses, storage facilities, manufacturing units, and other high-risk areas where early fire detection is critical.

---

# 🚀 Features

## 🔥 Real-Time Fire Detection

Detects visible fire from CCTV footage using a custom-trained YOLOv8 model.

## 💨 Smoke Detection

Detects smoke at an early stage before fire escalation.

## 📸 Automatic Screenshot Capture

Captures and stores evidence screenshots whenever a fire or smoke event is detected.

## 📝 Event Logging

Stores all incidents in CSV format with:

- Timestamp
- Event Type
- Detection Confidence

## 🚨 Alarm System

Plays an audible alarm whenever a fire or smoke event is detected.

## 📊 Live Dashboard

Provides:

- Total detected incidents
- Detection confidence analytics
- Event history
- Latest captured screenshot
- Interactive graphs
- Real-time monitoring

## 📈 Advanced Visualizations

Includes:

- Confidence Trend Graph
- 3D Confidence Analysis
- Detection Statistics
- Live Status Indicators

---

# 🏗️ System Architecture

```text
CCTV Feed
      │
      ▼
YOLOv8 Detection Engine
      │
      ▼
Fire / Smoke Detected
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼
Alarm Log Screenshot
 │      │      │
 └──────┴──────┘
        │
        ▼
 Streamlit Dashboard
```

---

# 📂 Project Structure

```text
IOCL-Fire-and-Smoke-Detection
│
├── dashboard.py
├── fire_monitor.py
├── logger.py
├── email_alert.py
├── alarm.mp3
├── api.py
│
├── logs
│   └── fire_log.csv
│
├── screenshots
│   └── captured images
├── _pycache_
│   └── api.cpython -312.pyc
│
├── runs/
│── test_data/
├── best weights of training YOLO v8
│   └── best.pt
│
├── custom_data.yaml
│
└── README.md
```

---

# 🛠️ Technologies Used

## Artificial Intelligence

- YOLOv8
- Ultralytics
- Deep Learning-based Object Detection
- Computer Vision

## Dashboard

- Streamlit
- Plotly
- Streamlit Auto Refresh

## Data Processing

- Pandas
- NumPy
- 
## Backend & APIs
- FastAPI
- Uvicorn
- Python Multipart

## Image Processing

- Pillow

## Alerts

- Playsound
- Automated Screenshot Capture
- Event Logging

## Deep Learning Frameworks
- PyTorch
- TorchVision

## Surveillance Sources
- Webcam Feed
- CCTV Feed
- Video File Processing
  
---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/mandrita16/IOCL-Fire-and-Smoke-Detection.git

cd IOCL-Fire-and-Smoke-Detection
```

---

## Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install ultralytics
pip install opencv-python
pip install pandas
pip install streamlit
pip install plotly
pip install pillow
pip install playsound
```

Or install directly from requirements.txt:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Fire Detection

Run the monitoring system:

```bash
python fire_monitor.py
```

The system will:

1. Open CCTV or video feed
2. Detect fire and smoke
3. Save screenshots
4. Trigger alarm
5. Update logs

---

# 📊 Running Dashboard

Launch dashboard:

```bash
streamlit run dashboard.py
```

Open browser:

```text
http://localhost:8501
```

---

# 📸 Dashboard Features

## Live Monitoring

Displays:

- Fire Events Count
- Detection Confidence
- Screenshot Count

## Visual Analytics

- Confidence Trend Graph
- 3D Confidence Visualization
- Detection Statistics

## Incident Tracking

- Latest Screenshot
- Event Logs
- Detection History

---

# 📄 Log File Format

Example:

```csv
Timestamp,Event,Confidence
2026-06-25_10-18-03,FIRE,0.775
2026-06-25_10-18-08,FIRE,0.705
2026-06-25_10-18-12,FIRE,0.704
```

---

# 🚨 Alarm Workflow

When fire or smoke is detected:

1. Detection confidence checked
2. Screenshot captured
3. CSV log updated
4. Alarm sound played
5. Dashboard refreshed

---

# 🔮 Future Enhancements

- Email Alerts
- SMS Notifications
- WhatsApp Alerts
- Multi-Camera Monitoring
- Cloud Deployment
- Mobile Application
- GIS Mapping
- Emergency Response Integration
- Incident Heatmaps
- Predictive Risk Analytics

---

# 🏭 Industrial Applications

This solution can be deployed in:

- Oil Refineries
- Chemical Plants
- Manufacturing Industries
- Warehouses
- Fuel Storage Units
- Smart Cities
- Industrial Campuses
- Forest Fire Monitoring Systems

---

# 🎯 Project Objectives

- Early Fire Detection
- Industrial Safety Enhancement
- Continuous Surveillance
- Automated Incident Reporting
- Reduced Human Monitoring Effort
- Faster Emergency Response

---

# 👩‍💻 Author

**Mandrita Dasgupta**

B.Tech Computer Science Engineering


---

# 📜 License

This project is developed for educational, research, and industrial safety applications.

---

