create database if not exists hospital;
use hospital;

-- Создание таблицы пациентов
CREATE TABLE if not exists  Patients (
    PatientID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    Age INT,
    Gender VARCHAR(10),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

-- Добавление данных в таблицу пациентов
INSERT INTO Patients (FullName, Age, Gender, Phone, Email, Address) VALUES
('John Smith', 35, 'Male', '+123456789', 'john@example.com', '123 Main St'),
('Anna Johnson', 28, 'Female', '+987654321', 'anna@example.com', '456 Oak St');

-- Создание таблицы врачей
CREATE TABLE if not exists Doctors (
    DoctorID INT AUTO_INCREMENT PRIMARY KEY,
    FullName VARCHAR(100),
    Specialization VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

-- Добавление данных в таблицу врачей
INSERT INTO Doctors (FullName, Specialization, Phone, Email, Address) VALUES
('Dr. Robert Brown', 'Cardiologist', '+111111111', 'robert@example.com', '789 Elm St'),
('Dr. Elena Petrova', 'Dermatologist', '+222222222', 'elena@example.com', '567 Pine St');

-- Создание таблицы медицинских записей
CREATE TABLE if not exists MedicalRecords (
    RecordID INT AUTO_INCREMENT PRIMARY KEY,
    PatientID INT,
    DoctorID INT,
    Diagnosis VARCHAR(255),
    Prescription VARCHAR(255),
    Date DATE,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
);

-- Добавление данных в таблицу медицинских записей
INSERT INTO MedicalRecords (PatientID, DoctorID, Diagnosis, Prescription, Date) VALUES
(1, 1, 'Hypertension', 'Prescribed medication X', '2023-01-15'),
(2, 2, 'Eczema', 'Recommended ointment Y', '2023-02-20');

-- Добавление дополнительных данных в таблицу пациентов
INSERT INTO Patients (FullName, Age, Gender, Phone, Email, Address) VALUES
('Emily Davis', 45, 'Female', '+444444444', 'emily@example.com', '789 Maple St'),
('Michael Brown', 50, 'Male', '+555555555', 'michael@example.com', '1010 Oak St');

-- Добавление дополнительных данных в таблицу врачей
INSERT INTO Doctors (FullName, Specialization, Phone, Email, Address) VALUES
('Dr. Maria Garcia', 'Pediatrician', '+333333333', 'maria@example.com', '234 Elm St'),
('Dr. Alex Johnson', 'Orthopedist', '+666666666', 'alex@example.com', '777 Pine St');

-- Добавление дополнительных данных в таблицу медицинских записей
INSERT INTO MedicalRecords (PatientID, DoctorID, Diagnosis, Prescription, Date) VALUES
(1, 3, 'Flu', 'Prescribed medication Z', '2023-03-10'),
(2, 4, 'Fractured arm', 'Recommended rest and splint', '2023-04-05');

-- Добавление дополнительных данных в таблицу пациентов
INSERT INTO Patients (FullName, Age, Gender, Phone, Email, Address) VALUES
('Olivia Wilson', 32, 'Female', '+777777777', 'olivia@example.com', '321 Oak St'),
('Daniel Miller', 60, 'Male', '+888888888', 'daniel@example.com', '456 Maple St');

-- Добавление дополнительных данных в таблицу врачей
INSERT INTO Doctors (FullName, Specialization, Phone, Email, Address) VALUES
('Dr. Jessica Lee', 'Neurologist', '+999999999', 'jessica@example.com', '888 Elm St'),
('Dr. William Clark', 'Psychiatrist', '+1010101010', 'william@example.com', '999 Pine St');

-- Добавление дополнительных данных в таблицу медицинских записей
INSERT INTO MedicalRecords (PatientID, DoctorID, Diagnosis, Prescription, Date) VALUES
(3, 5, 'Migraine', 'Prescribed medication A', '2023-05-20'),
(4, 6, 'Anxiety disorder', 'Counseling sessions', '2023-06-15');
