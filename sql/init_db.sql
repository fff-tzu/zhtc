-- 告诉别人先创建库
CREATE DATABASE IF NOT EXISTS `zhtc_db`;
USE `zhtc_db`;

-- 创建你选定的 users 表
CREATE TABLE IF NOT EXISTS `users` (
                                       `id` int NOT NULL AUTO_INCREMENT,
                                       `username` varchar(50) NOT NULL,
    `password` varchar(50) NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;