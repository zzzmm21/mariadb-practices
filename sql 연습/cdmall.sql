create database cdmall;

create user 'cd'@'localhost' identified by 'cdmall';
grant all privileges on cdmall.* to 'cd'@'localhost';

flush privileges; 

