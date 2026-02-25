CREATE DATABASE CAMERA_FILE;
use CAMERA_FILE;
CREATE TABLE record_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clip_id INT,
    recording_date DATE,
    start_time DATETIME,
    end_time DATETIME,
    duration_seoconds INT,
    file_name VARCHAR(255),
    file_path VARCHAR(255)
);
ALTER TABLE record_data CHANGE duration_seoconds duration_seconds int;