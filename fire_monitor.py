import cv2
import os
import csv
import time
import winsound
from playsound import playsound
from datetime import datetime
from ultralytics import YOLO
from email_alert import send_fire_alert
# ======================
# CONFIG
# ======================

MODEL_PATH = r"best weights of training YOLO v8\best_v8.pt"

CONFIDENCE_THRESHOLD = 0.60

PERSISTENCE_FRAMES = 30

SCREENSHOT_DIR = "screenshots"

LOG_FILE = "logs/fire_log.csv"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs("logs", exist_ok=True)

# ======================
# LOAD MODEL
# ======================

model = YOLO(MODEL_PATH)

# ======================
# LOG FILE
# ======================

if not os.path.exists(LOG_FILE):

    with open(LOG_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Timestamp",
            "Event",
            "Confidence"
        ])

# ======================
# CCTV SOURCE
# ======================

import glob

video_files = glob.glob("test_data/*.mp4")

print("Videos Found:")
for v in video_files:
    print(v)

# For CCTV later:
# cap = cv2.VideoCapture("rtsp://camera_ip/live")
last_first_time = 0
COOLDOWN_SECONDS = 20
fire_counter = 0

latest_status = "SAFE"

print("System Started...")

for video_path in video_files:

    print(f"\nProcessing: {video_path}")

    cap = cv2.VideoCapture(video_path)

    fire_counter = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        fire_detected = False
        smoke_detected = False

        highest_conf = 0

        for result in results:

            boxes = result.boxes

            for box in boxes:

                cls = int(box.cls[0])

                conf = float(box.conf[0])

                label = model.names[cls]

                if conf < CONFIDENCE_THRESHOLD:
                    continue

                if conf > highest_conf:
                    highest_conf = conf
                    print("Detected label:", label)

                if label.lower() == "fire":
                    fire_detected = True

                if "smoke" in label.lower():
                    smoke_detected = True

        if fire_detected:
            fire_counter += 1
            print(f"Fire Counter = {fire_counter}")
        else:
            fire_counter = 0

        if (
            fire_counter >= PERSISTENCE_FRAMES
            and
            time.time()-last_first_time>COOLDOWN_SECONDS
        ):
            timestamp = datetime.now().strftime(
                "%Y-%m-%d_%H-%M-%S"
            )

            screenshot_path = os.path.join(
                SCREENSHOT_DIR,
                f"fire_{timestamp}.jpg"
            )

            cv2.imwrite(
                screenshot_path,
                frame
            )
            send_fire_alert(
                round(highest_conf,3)
            )
            last_first_time = time.time()
            with open(LOG_FILE, "a", newline="") as f:

                writer = csv.writer(f)

                writer.writerow([
                    timestamp,
                    "FIRE",
                    round(highest_conf, 3)
                ])

            playsound("alarm.mp3")

            print(
                f"FIRE DETECTED {highest_conf:.2f}"
            )

            fire_counter = 0

        annotated = results[0].plot()
        cv2.imwrite(
          "live_frame.jpg",
           annotated
          )

        cv2.putText(
            annotated,
            f"STATUS: {'FIRE' if fire_detected else 'SAFE'}",
            (20,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        cv2.imshow(
            "IOCL Fire Monitoring",
            annotated
        )

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()

   
cv2.destroyAllWindows()