-- Create the database
CREATE DATABASE IF NOT EXISTS iot_db;

-- Use the database
USE iot_db;

-- Create the table
CREATE TABLE IF NOT EXISTS iot_tbl (
    id INT AUTO_INCREMENT PRIMARY KEY,
    created_at DATETIME UNIQUE,
    temperature FLOAT,
    humidity FLOAT,
    atmospheric_pressure FLOAT,
    gas FLOAT,
    wind_speed FLOAT,
    precipitation FLOAT,
    wind_direction FLOAT,
    uv FLOAT
);
