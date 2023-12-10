create database if not exists hospital;
use hospital;
/*
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





-- Добавление дополнительных данных в таблицу медицинских записей
INSERT INTO MedicalRecords (PatientID, DoctorID, Diagnosis, Prescription, Date) VALUES
(4, 1, 'Migraine', 'Prescribed medication A', '2023-12-01'),
(3, 2, 'Anxiety disorder', 'Counseling sessions', '2023-12-03');

-- Добавление дополнительных данных в таблицу медицинских записей
INSERT INTO MedicalRecords (PatientID, DoctorID, Diagnosis, Prescription, Date) VALUES
(2, 1, 'Migraine', 'Prescribed medication B', '2023-03-30'),
(1, 2, 'Anxiety disorder', 'Counseling sessions', '2023-07-15');

-- Добавление дополнительных данных в таблицу пациентов
INSERT INTO Patients (FullName, Age, Gender, Phone, Email, Address) VALUES
('Olivia Ivanova', 33, 'Female', '+777777777', 'olivia@example.com', '321 Oak St'),
('Olga Onapova', 44, 'Male', '+888888888', 'daniel@example.com', '456 Maple St');

-- Добавление дополнительных данных в таблицу врачей
INSERT INTO Doctors (FullName, Specialization, Phone, Email, Address) VALUES
('Dr. Jessica Loo', 'Neurologist', '+999999999', 'Jessica@example.com', '888 Elm St'),
('Dr. Monko Roo', 'Psychiatrist', '+1010101010', 'Monko@example.com', '999 Pine St');

*/

-- показать все записи приемов
-- показать все записи данного доктора
-- показать все записи данного клиента
/* показать все записи на прием*/
-- select * from MedicalRecords;
 
/* показать все записи доктора Dr. Robert Brown*/
-- select * from MedicalRecords
-- join Doctors
-- on MedicalRecords.DoctorID = Doctors.DoctorID
-- and FullName = 'Dr. Robert Brown';
 
/* показать все записи пациента Emily Davis*/
-- select * from MedicalRecords
-- join Patients
-- on MedicalRecords.PatientID = Patients.PatientID
-- and FullName = 'Emily Davis';


--  показать даты ближайшего приема 
--  показать кол-во записией у данного врача
-- показать кол-во посещений у данного клиента
/* показать дату ближайшего(последнего) приема */
-- select max(Date) from MedicalRecords;

/* показать дату  3 ближайших(последнего) приема */
-- select * from MedicalRecords where Date <= current_date() order by date desc limit 3;
 
/* показать кол-во записей у доктора Dr. Elena Petrova */
-- select count(PatientID) from MedicalRecords
-- join Doctors
-- on MedicalRecords.DoctorID = Doctors.DoctorID
-- and FullName = 'Dr. Elena Petrova';
 
/* показать кол-во посещений у пациента John Smith */
-- select count(DoctorID) from MedicalRecords
-- join Patients
-- on MedicalRecords.PatientID = Patients.PatientID
-- and FullName = 'John Smith';




/* показать все записи пациентов в том, числе у которых нет записи на прием*/
/* показать все записи врачей в том, числе у которых нет записи на прием*/
--  показать самый давний (первый) прием данного пациента 

/* показать все записи пациентов в том, числе у которых нет записи на прием */
-- select * from MedicalRecords
-- right join Patients
-- on MedicalRecords.PatientID = Patients.PatientID;
 
/* показать все записи врачей в том, числе у которых нет записи на прием */
-- select * from Doctors
-- left join MedicalRecords
-- on MedicalRecords.DoctorID = Doctors.DoctorID;
 
 
 /* показать  врачей и пациентов в том, числе у которых нет записи на прием */
/* select  RecordID, FullName, Specialization, Phone, Email, Address from MedicalRecords
right join Doctors
on MedicalRecords.DoctorID = Doctors.DoctorID where RecordID is NULL
UNION
select RecordID, FullName, Gender, Phone, Email, Address from MedicalRecords
right join Patients
on MedicalRecords.PatientID = Patients.PatientID where RecordID is NULL;
*/

/* показать самый давний (ранний) прием у пациента Anna Johnson */
-- select * from MedicalRecords, Patients 
-- where Date <= current_date()
-- and FullName = 'Anna Johnson' 
-- and MedicalRecords.PatientID = Patients.PatientID limit 1;


-- показать самого популярного врача (у него больше всего записей)*
/*select count(RecordID), FullName  from MedicalRecords
join Doctors
on MedicalRecords.DoctorID = Doctors.DoctorID group by FullName order by count(RecordID) desc limit 1;
*/

/*
select count(RecordID) as amount, FullName  from MedicalRecords
join Doctors
on MedicalRecords.DoctorID = Doctors.DoctorID group by FullName  having amount> 1;*/



-- показать самую непопулярную болезнь (встречается меньше всего записей)
/* select count(RecordID), Diagnosis from MedicalRecords
group by Diagnosis having count(RecordID) <= 1; */
/*
select count(RecordID), Diagnosis from MedicalRecords
group by Diagnosis order by count(RecordID) limit 5; */

-- найти разницу между первым и последним посещением клиента 
SELECT datediff(MAX(MedicalRecords.Date), MIN(MedicalRecords.Date)) from MedicalRecords;
SELECT 
    Patients.FullName,
    datediff(MAX(MedicalRecords.Date),MIN(MedicalRecords.Date)) -- datediff () вычисляет разницу дней
FROM
    patients
        JOIN
    medicalrecords ON MedicalRecords.PatientID = Patients.PatientID
GROUP BY Patients.PatientID;

-- показать клиента, который не посещал ни разу врачей (в данной бд)
-- показать клиента, который не посещал врачей за последний полгода
















