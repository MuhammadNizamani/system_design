CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123';
CREATE DATABASE auth;
GRANT ALL PRIVILEGES ON auth.* To 'auth_user'@'localhost';
USE auth;
CREATE TABLE user(
    id INT NOT NULL AUTO_INCRIMENT PRIMARY KEY
    email VARCHAR(255) NOT NULL
    password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('ishaque@gmail.com', 'password');