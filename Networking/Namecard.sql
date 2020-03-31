DROP DATABASE IF EXISTS namecard;
CREATE DATABASE namecard;
USE namecard;

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
  PRIMARY KEY (cid, uid)
);

INSERT INTO namecards VALUES
("sherman", 1, 'Robert Downey Jr', 'debwahlee@gmail.com', 87654321, 'Avengers', 'Data Analyst', 'Superhero'),
("sherman", 2, 'Chris Evan', 'deborah.lee.2018@sis.smu.edu.sg', 98765432, 'Avengers', 'COO', 'Superhero');



