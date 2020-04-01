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
("sherman", 1, 'Sherman Lee', 'sherman.lee.2018@sis.smu.edu.sg', 87654321, 'ABC Limited', 'Data Analyst', 'Analytics'),
("shishiong", 2, 'Neo Shi Shiong', 'ssneo.2018@sis.smu.edu.sg', 98765432, 'Decathlon', 'Associate', 'Marketing'),
("ruipeng", 3, 'Lee Rui Peng', 'ruipeng.lee.2018@sis.smu.edu.sg', 96492746, 'Siemens', 'Associate', 'IT'),
("rachel", 4, 'Rachel Lui', 'rachel.lui.2018@sis.smu.edu.sg', 91623784, 'Shopee', 'Associate', 'Marketing'),
("pooja", 5, 'Pooja Kumar', 'poojakumar.2018@sis.smu.edu.sg', 99173264, 'ABC Limited', 'Support Staff', 'IT'),
("deborah", 6, 'Deborah Lee', 'deborah.lee.2018@sis.smu.edu.sg', 93715409, 'Toko', 'Associate', 'IT'),
("tom", 7, 'Tom How', 'tom.how.2017@sob.smu.edu.sg', 98768142, 'Siemens', 'Associate', 'Advertising'),
("john", 8, 'John Low', 'john.low.2018@sob.smu.edu.sg', 95412680, 'Decathlon', 'Support Staff', 'IT'),
("shurui", 9, 'Wang Shu Rui', 'shurui.wang.2019@sis.smu.edu.sg', 96132654, 'ABC Limited', 'Associate', 'Analytics'),
("megan", 10, 'Megan Goh', 'megan.goh.2019@sob.smu.edu.sg', 82538751, 'SMU Verts', 'Director', 'Marketing')
;
