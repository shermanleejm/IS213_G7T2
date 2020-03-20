-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 20, 2020 at 04:28 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `NAP`
--
CREATE DATABASE IF NOT EXISTS `NAP` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `NAP`;

-- --------------------------------------------------------

--
-- Table structure for table `mailing`
--

DROP TABLE IF EXISTS `mailing`;
CREATE TABLE `mailing` (
  `mailid` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `maildate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mailstatus` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `namecards`
--

DROP TABLE IF EXISTS `namecards`;
CREATE TABLE `namecards` (
  `uid` varchar(8) NOT NULL,
  `cid` varchar(8) NOT NULL,
  `name` char(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_num` int(8) DEFAULT NULL,
  `company` char(100) NOT NULL,
  `title` char(100) NOT NULL,
  `industry` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `namecards`
--

INSERT INTO `namecards` (`uid`, `cid`, `name`, `email`, `phone_num`, `company`, `title`, `industry`) VALUES
('U001', 'C1', 'Robert Downey Jr', 'debwahlee@gmail.com', 87654321, 'Avengers', 'Data Analyst', 'Superhero'),
('U002', 'C1', 'Chris Evan', 'deborah.lee.2018@sis.smu.edu.sg', 98765432, 'Avengers', 'COO', 'Superhero');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `uid` varchar(8) NOT NULL,
  `name` char(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pword` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`uid`, `name`, `email`, `pword`) VALUES
('U001', 'Deborah Lee', 'deborah.lee.2018@sis.smu.edu.sg', 'apple123'),
('U002', 'Rachel Lui', 'rachel.lui.2018@sis.smu.edu.sg', 'orange123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mailing`
--
ALTER TABLE `mailing`
  ADD PRIMARY KEY (`mailid`);

--
-- Indexes for table `namecards`
--
ALTER TABLE `namecards`
  ADD PRIMARY KEY (`uid`,`cid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `namecards`
--
ALTER TABLE `namecards`
  ADD CONSTRAINT `namecards_fk` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`);
