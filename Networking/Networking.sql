-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 06, 2020 at 10:21 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `Networking`
--
CREATE DATABASE IF NOT EXISTS `Networking` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `Networking`;

-- --------------------------------------------------------

--
-- Table structure for table `Namecards`
--

DROP TABLE IF EXISTS `Namecards`;
CREATE TABLE `Namecards` (
  `uid` char(8) NOT NULL,
  `cid` char(8) NOT NULL,
  `name` char(100) NOT NULL,
  `email` char(100) NOT NULL,
  `phone_num` int(8) DEFAULT NULL,
  `company` char(100) NOT NULL,
  `title` char(100) NOT NULL,
  `industry` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
CREATE TABLE `Users` (
  `uid` char(8) NOT NULL,
  `name` char(100) NOT NULL,
  `email` char(100) NOT NULL,
  `pword` char(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Namecards`
--
ALTER TABLE `Namecards`
  ADD PRIMARY KEY (`uid`,`cid`);

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`uid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Namecards`
--
ALTER TABLE `Namecards`
  ADD CONSTRAINT `namecards_fk` FOREIGN KEY (`uid`) REFERENCES `users` (`uid`);
