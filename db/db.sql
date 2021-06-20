CREATE DATABASE IF NOT EXISTS `temperatura`;
use `temperatura`;


CREATE TABLE IF NOT EXISTS `data`(
`id` int NOT NULL AUTO_INCREMENT,
`temperature` DECIMAL(15,2),
`date_with_time` TIMESTAMP,
PRIMARY KEY (`id`)

);
