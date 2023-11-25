create database if not exists test;
use test;

create table if not exists players(
	name_p varchar(20) default "player", -- default - по умоланию
	best_score int default 0
);
-- drop table if exists player;





-- drop database if exists test;