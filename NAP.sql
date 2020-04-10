DROP DATABASE IF EXISTS user;
CREATE DATABASE user;
USE user;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  uid varchar(30) NOT NULL ,
  name char(100) NOT NULL,
  email varchar(100) NOT NULL,
  password text(1000) NOT NULL,
  emailpassword text(1000) NOT NULL,
  PRIMARY KEY (uid)
);

INSERT INTO users VALUES
("admin", "Lee Sherman", "sherman.lee.2018@sis.smu.edu.sg", "shermanrox", "$6$rounds=656000$rjYYcRc.ZGJbYt16$xYRPewN4Ph5IP7fTBkPPWxzDkqzgjR2LqLTyOIr5TxGn5Z1Q3zbISiBmFiuCXHhNMQiYd1ua4GcU9wrBxnAAa0")
;

DROP DATABASE IF EXISTS namecard;
CREATE DATABASE namecard;
USE namecard;

DROP TABLE IF EXISTS namecards;
CREATE TABLE namecards (
  uid varchar(30) NOT NULL,
  name varchar(100) NOT NULL,
  email varchar(100) NOT NULL,
  phone_num int NOT NULL,
  company varchar(100) NOT NULL,
  title varchar(100) NOT NULL,
  industry varchar(100) NOT NULL,
  PRIMARY KEY (uid, name, email, phone_num, company, title, industry)
);

INSERT INTO namecards VALUES
("admin", 'Sherman Lee', 'sherman.lee.2018@sis.smu.edu.sg', 87654321, 'ABC Limited', 'Data Analyst', 'Analytics'),
("admin",  'Neo Shi Shiong', 'ssneo.2018@sis.smu.edu.sg', 98765432, 'Decathlon', 'Associate', 'Marketing'),
("admin",  'Lee Rui Peng', 'ruipeng.lee.2018@sis.smu.edu.sg', 96492746, 'Siemens', 'Associate', 'IT'),
("admin",  'Rachel Lui', 'rachel.lui.2018@sis.smu.edu.sg', 91623784, 'Shopee', 'Associate', 'Marketing'),
("admin",  'Pooja Kumar', 'poojakumar.2018@sis.smu.edu.sg', 99173264, 'ABC Limited', 'Support Staff', 'IT'),
("admin",  'Deborah Lee', 'deborah.lee.2018@sis.smu.edu.sg', 93715409, 'Toko', 'Associate', 'IT'),
("admin",  'Tom How', 'tom.how.2017@sob.smu.edu.sg', 98768142, 'Siemens', 'Associate', 'Advertising'),
("admin",  'John Low', 'john.low.2018@sob.smu.edu.sg', 95412680, 'Decathlon', 'Support Staff', 'IT'),
("admin",  'Wang Shu Rui', 'shurui.wang.2019@sis.smu.edu.sg', 96132654, 'ABC Limited', 'Associate', 'Analytics'),
("admin",  'Megan Goh', 'megan.goh.2019@sob.smu.edu.sg', 82538751, 'SMU Verts', 'Director', 'Marketing')
;
