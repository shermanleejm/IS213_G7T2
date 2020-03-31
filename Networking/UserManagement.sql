DROP DATABASE IF EXISTS UserManagement;
CREATE DATABASE UserManagement;
USE UserManagement;


DROP TABLE IF EXISTS users;
CREATE TABLE users (
  uid varchar(30) NOT NULL ,
  name char(100) NOT NULL,
  email varchar(100) NOT NULL,
  password text(1000) NOT NULL,
  PRIMARY KEY (uid)
);


INSERT INTO users VALUES
(1, 'Deborah Lee', 'deborah.lee.2018@sis.smu.edu.sg', 'apple123'),
(2, 'Rachel Lui', 'rachel.lui.2018@sis.smu.edu.sg', 'orange123');
