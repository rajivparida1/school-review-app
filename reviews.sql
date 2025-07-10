CREATE DATABASE IF NOT EXISTS school_reviews;
USE school_reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100),
    reviewer_name VARCHAR(100),
    rating INT,
    comment TEXT
);
