CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

CREATE TABLE IF NOT EXISTS hotel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    adresse TEXT
);

CREATE TABLE IF NOT EXISTS chambre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero VARCHAR(20) NOT NULL,
    type ENUM('simple', 'double', 'suite') NOT NULL,
    prix DECIMAL(10,2) NOT NULL,
    etat ENUM('libre', 'occupee', 'maintenance') DEFAULT 'libre',
    hotel_id INT,
    FOREIGN KEY (hotel_id) REFERENCES hotel(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS client (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    tel VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    chambre_id INT,
    date_debut DATE NOT NULL,
    date_fin DATE NOT NULL,
    status ENUM('confirmee', 'annulee') DEFAULT 'confirmee',
    FOREIGN KEY (client_id) REFERENCES client(id) ON DELETE CASCADE,
    FOREIGN KEY (chambre_id) REFERENCES chambre(id) ON DELETE CASCADE
);

CREATE USER IF NOT EXISTS 'userdb'@'%' IDENTIFIED BY 'userdb';

GRANT ALL PRIVILEGES ON hotel_db.* TO 'userdb'@'%';

FLUSH PRIVILEGES;
