/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.7.11 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `douban_books` (
	`id` int (11),
	`name` varchar (300),
	`author` varchar (300),
	`press` varchar (300),
	`date` varchar (90),
	`page` varchar (90),
	`price` varchar (90),
	`score` varchar (90),
	`rating_people` varchar (33),
	`ISBN` varchar (90),
	`subject_id` varchar (33),
	`tags` varchar (2400)
); 
