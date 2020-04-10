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
