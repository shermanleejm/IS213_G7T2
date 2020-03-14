-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 14, 2020 at 03:13 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nap`
--

-- --------------------------------------------------------

--
-- Table structure for table `mailing`
--

DROP TABLE IF EXISTS `mailing`;
CREATE TABLE IF NOT EXISTS `mailing` (
  `mailid` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `maildate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mailstatus` varchar(100) NOT NULL,
  PRIMARY KEY (`mailid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `namecards`
--

DROP TABLE IF EXISTS `namecards`;
CREATE TABLE IF NOT EXISTS `namecards` (
  `uid` varchar(8) NOT NULL,
  `cid` varchar(8) NOT NULL,
  `name` char(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_num` int(8) DEFAULT NULL,
  `company` char(100) NOT NULL,
  `title` char(100) NOT NULL,
  `industry` char(100) NOT NULL,
  PRIMARY KEY (`uid`,`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `uid` varchar(8) NOT NULL,
  `name` char(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pword` char(100) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `namecards`
--
ALTER TABLE `namecards`
  ADD CONSTRAINT `namecards_fk` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
