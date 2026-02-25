CREATE DATABASE camera_file;

USE camera_file;

CREATE TABLE record_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    clip_id INT,
    recording_date DATE,
    start_time DATETIME,
    end_time DATETIME,
    duration_seconds INT,
    file_name VARCHAR(255),
    file_path VARCHAR(255)
);
