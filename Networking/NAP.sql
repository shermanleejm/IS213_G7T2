-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 28, 2020 at 01:41 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `nap`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `uid` varchar(30) NOT NULL,
  `name` char(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`uid`, `name`, `email`, `password`) VALUES
('1', 'Deborah Lee', 'deborah.lee.2018@sis.smu.edu.sg', 'apple123'),
('2', 'Rachel Lui', 'rachel.lui.2018@sis.smu.edu.sg', 'orange123'),
('5', 'robert', '123', '$6$rounds=656000$58UT3x6NPDYB1gGO$Au66cjZB88fzPETDgQBO4ku6vxHelXGpnBl/Qb/wKJyNjLG5ZPNM1DSYM..yHeTGG5BVoFKonLZ/q4ZOIobpr0'),
('6', '6', '6', '$6$rounds=656000$vfxvSMin8ozPAgSd$e9RDEqr/c7uyGr4iBppEFWAi/hfuOSshCG4cwzlAtORZ/rYd1IDLIBhiN0CO6mHtyyT7z9Mwa2nh1oOBH2XPC/'),
('Big B', 'Blair Waldof', 'BW@nap.com', '$6$rounds=656000$rvDJq5nPldUeG5SI$wZ1nxah0zGT1.Guze03sqCc5CgsGEY1WhDkMoPCoMgGnK7VPIJdZiM/rUmdO.yUj8UJUtG.yFZiyS3o9cn3wk/'),
('deebo', 'deebo', 'deebo', '$6$rounds=656000$K.48fx5U0P2f/feU$bNPgGVZ2Xn05UyZT6TLFXCW6qFTEnWbu2SlFg4a2xw9tFslg8xTiUbC6IYBot6cKujIUXQk.wfIOdBNNjVClT.'),
('hihi', 'hi', 'hu@gmail.com', '$6$rounds=656000$U9CQyfj2UxlLOIpG$gjvCErN0GKoOwRuLi2zm5Fm6cTMJEfXDVYSHodpcUoT/GxR6FAT0QOErkLC2/p5g2JWfA6P9M/T6e/Mbt68le.'),
('name', 'name', 'name', '$6$rounds=656000$WEKXNNE4J6NFJvLU$80i//Ghm3tuLf.xGkoSOqC3gODCSNubRG8NWa2yVeqwhUxREAI1ybjsqB9ZWrrwI5lbsgTbFmOXueZiQZjzBl0'),
('robert234', 'robert', 'hu@gmail.com', '$6$rounds=656000$TpXOV7JSWVeRVqC/$C3POOHkoFoz/jtQZloPCDEGWYpay00dzq49S8nT8PJfRNGx1M7vape3HlqDgQihdcInZIxn0xOUv4fH8tMa4X.'),
('S', 'serena vanderwoodsen', 'SVW@nap.com', '$6$rounds=656000$cR5ABW8gTxCNR8w0$vRXCoz.TUuwsMv.4ePXKnqBYczsf.c5OP0i1dc7r89hHiKQgaKnpn6ry5vdv3hjw6nssAtVsOSaGtNQ7dFjFq0'),
('second', 'robert', 'jkl@', '$6$rounds=656000$N9b.HmALCb5Nvb4G$sNTIRKdkmFERgmRDksyk.EPr/WmL9LwEWq/KGl404Da0WksFtFB.va7jA4qI1s.sWobx3W6smZExv4ydzUt3x0'),
('tester', 'test tan', 'iu@gmail.com', '$6$rounds=656000$aqApz/jPZRdNJ5jI$v5hGwShzE6E9fs90F7aco/qhEJjSIp./0aBTl4CLYsNjI.W2gOn9.weQ5b.EEyINRYmqr8nwnRLKsi61ambGx0');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`uid`);
