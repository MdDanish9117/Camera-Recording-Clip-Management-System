import cv2
import os
import time
from datetime import datetime
import mysql.connector

# 1. User input
total_min = int(input("Total recording minutes: "))
interval_min = int(input("Clip interval minutes: "))

total_sec = total_min * 60
interval_sec = interval_min * 60

# 2. Folder create
if not os.path.exists("recordings"):
    os.mkdir("recordings")

# 3️. Database connect
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CAMERA_FILE"
)
cursor = db.cursor()

# 4️. Camera start
camera = cv2.VideoCapture(0)

start_time = time.time()
clip_no = 1

while time.time() - start_time < total_sec:

    clip_start = datetime.now()
    file_name = f"clip_{clip_no}.mp4"
    file_path = "recordings/" + file_name

    writer = cv2.VideoWriter(
        file_path,
        cv2.VideoWriter_fourcc(*'mp4v'),
        20,
        (640, 480)
    )

    clip_timer = time.time()

    while time.time() - clip_timer < interval_sec:
        ret, frame = camera.read()
        if ret:
            writer.write(frame)

    writer.release()

    clip_end = datetime.now()
    duration = int((clip_end - clip_start).total_seconds())

    # Data insert
    cursor.execute(
        "INSERT INTO record_data (clip_id, recording_date, start_time, end_time, duration_seconds, file_name, file_path) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        (clip_no, clip_start.date(), clip_start, clip_end, duration, file_name, file_path)
    )
    db.commit()

    print("Saved:", file_name)

    clip_no += 1

camera.release()
db.close()

print("Recording Completed")