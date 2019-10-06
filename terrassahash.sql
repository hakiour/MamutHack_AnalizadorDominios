-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 06, 2019 at 02:02 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `terrassahash`
--

-- --------------------------------------------------------

--
-- Table structure for table `dominio`
--

CREATE TABLE `dominio` (
  `idDominio` int(11) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `ipUsuario` varchar(45) NOT NULL,
  `nombreDominio` varchar(100) NOT NULL,
  `tematica` varchar(100) NOT NULL,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dominio`
--

INSERT INTO `dominio` (`idDominio`, `fecha`, `ipUsuario`, `nombreDominio`, `tematica`, `created`) VALUES
(1, '2019-10-05 22:44:48', '192.168.1.9', 'lavanguardia.com', 'racismo', '2019-10-05 22:44:48'),
(2, '2019-10-05 22:45:07', '192.168.1.9', 'lavanguardia.com', 'racismo', '2019-10-05 22:45:07'),
(3, '2019-10-05 22:46:48', '192.168.1.9', 'facebook.com', 'racismo', '2019-10-05 22:46:48'),
(4, '2019-10-05 22:46:48', '192.168.1.9', 'twitter.com', 'racismo', '2019-10-05 22:46:48'),
(5, '2019-10-05 22:46:48', '192.168.1.9', 'mamuthack.com', 'racismo', '2019-10-05 22:46:48'),
(6, '2019-10-05 22:46:48', '192.168.1.9', 'https://www.forocoches.com/foro/showthread.php?t=6539653&page=2', 'racismo', '2019-10-05 22:46:48');

-- --------------------------------------------------------

--
-- Table structure for table `link`
--

CREATE TABLE `link` (
  `idLink` int(11) NOT NULL,
  `idDominio` int(11) NOT NULL,
  `indice` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `link`
--

INSERT INTO `link` (`idLink`, `idDominio`, `indice`) VALUES
(1, 1, 1),
(2, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `palabras`
--

CREATE TABLE `palabras` (
  `idPalabras` int(11) NOT NULL,
  `Palabra` varchar(50) NOT NULL,
  `tipo` varchar(50) NOT NULL,
  `numeroVeces` int(11) NOT NULL,
  `idLink` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `palabras`
--

INSERT INTO `palabras` (`idPalabras`, `Palabra`, `tipo`, `numeroVeces`, `idLink`) VALUES
(1, 'puto', '1', 23, 1),
(2, 'negrata', '2', 12, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dominio`
--
ALTER TABLE `dominio`
  ADD PRIMARY KEY (`idDominio`);

--
-- Indexes for table `link`
--
ALTER TABLE `link`
  ADD PRIMARY KEY (`idLink`);

--
-- Indexes for table `palabras`
--
ALTER TABLE `palabras`
  ADD PRIMARY KEY (`idPalabras`),
  ADD KEY `fkIdLink` (`idLink`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dominio`
--
ALTER TABLE `dominio`
  MODIFY `idDominio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `link`
--
ALTER TABLE `link`
  MODIFY `idLink` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `palabras`
--
ALTER TABLE `palabras`
  MODIFY `idPalabras` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `link`
--
ALTER TABLE `link`
  ADD CONSTRAINT `fkIdDominio` FOREIGN KEY (`idLink`) REFERENCES `dominio` (`idDominio`) ON DELETE CASCADE;

--
-- Constraints for table `palabras`
--
ALTER TABLE `palabras`
  ADD CONSTRAINT `fkIdLink` FOREIGN KEY (`idLink`) REFERENCES `link` (`idLink`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
