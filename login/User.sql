DROP DATABASE IF EXISTS userr;
CREATE DATABASE userr;
USE userr;

DROP TABLE IF EXISTS myuser;
CREATE TABLE myuser (
  uid varchar(30) NOT NULL ,
  name char(100) NOT NULL,
  email varchar(100) NOT NULL,
  password text(1000) NOT NULL,
  PRIMARY KEY (uid)
);

INSERT INTO myuser VALUES
("deebo", 'Deborah Lee', 'deborah.lee.2018@sis.smu.edu.sg', 'apple123'),
("rach", 'Rachel Lui', 'rachel.lui.2018@sis.smu.edu.sg', 'orange123'),
("sherman", "Lee Sherman", "sherman.lee.2018@sis.smu.edu.sg", "shermanrox")
;