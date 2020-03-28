DROP DATABASE IF EXISTS nap;
CREATE DATABASE nap;
USE nap;

DROP TABLE IF EXISTS mailing;
CREATE TABLE mailing (
  mailid int NOT NULL AUTO_INCREMENT,
  email varchar(100) NOT NULL,
  maildate datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  mailstatus varchar(100) NOT NULL,
  PRIMARY KEY (mailid)
);

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

DROP TABLE IF EXISTS namecards;
CREATE TABLE namecards (
  uid varchar(30) NOT NULL,
  cid INT AUTO_INCREMENT ,
  name varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  phone_num int NOT NULL,
  company varchar(100) NOT NULL,
  title varchar(100) NOT NULL,
  industry varchar(100) NOT NULL,
  PRIMARY KEY (cid, uid),
  FOREIGN KEY (uid) REFERENCES users(uid)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

INSERT INTO namecards VALUES
(1, 1, 'Robert Downey Jr', 'debwahlee@gmail.com', 87654321, 'Avengers', 'Data Analyst', 'Superhero'),
(1, 2, 'Chris Evan', 'deborah.lee.2018@sis.smu.edu.sg', 98765432, 'Avengers', 'COO', 'Superhero');
