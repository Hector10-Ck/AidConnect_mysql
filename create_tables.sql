-- Run this in MySQL to create the database schema for AidConnect
CREATE DATABASE IF NOT EXISTS aidconnect_db;
USE aidconnect_db;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(120),
  email VARCHAR(150) UNIQUE,
  password_hash VARCHAR(255),
  role ENUM('beneficiary','provider') DEFAULT 'beneficiary',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS aid_listings (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(200),
  category VARCHAR(100),
  description TEXT,
  location VARCHAR(200),
  posted_by INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (posted_by) REFERENCES users(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS requests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  listing_id INT,
  message TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (listing_id) REFERENCES aid_listings(id) ON DELETE CASCADE
);
