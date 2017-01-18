/*
 * how to use this menu.sql file?
 * start a mysql with the command: mysql -u root -p
 * enter the password: 123456
 * then run the command to execute this file: source menu.sql
 */
create database menu;
use menu;

drop table if exists fish;

set @saved_cs_client = @@character_set_client;
set character_set_client = utf8;

create table fish (
  ID int(11) not null auto_increment,
  NAME varchar(30) not null default '',
  PRICE decimal(5,2) not null default 0.00,
  primary key (ID)
) engine=MyISAM auto_increment=27 default charset=latin1;

set character_set_client = @saved_cs_client;

lock tables fish write;

INSERT INTO fish VALUES
(1,'catfish','8.50'),
(2,'catfish','8.50'),
(3,'tuna','8.00'),
(4,'catfish','5.00'),
(5,'bass','6.75'),
(6,'haddock','6.50'),
(7,'salmon','9.50'),
(8,'trout','6.00'),
(9,'tuna','7.50'),
(10,'yellowfin tuna','12.00'),
(11,'yellowfin tuna','13.00'),
(12,'tuna','7.50');
unlock tables;
