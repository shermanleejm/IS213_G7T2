DROP DATABASE IF EXISTS Namecard;
CREATE DATABASE Namecard;
USE Namecard;

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



