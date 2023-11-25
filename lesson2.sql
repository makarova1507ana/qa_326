create database if not exists test;
use test;

create table if not exists players(
	id int primary key AUTO_INCREMENT,
	name_p varchar(20) default "player", -- default - по умоланию
	best_score int default 0
);
-- drop table if exists player;

-- insert into players(name_p, best_score) values
-- ("Ivan", 2200),
-- ("Irakli", 100),
-- ("Masha", 550);

select * from players;

create table if not exists games(
	id int primary key AUTO_INCREMENT,
	name_player varchar(20) default "player", 
	score int default 0,
    id_player INT,
    FOREIGN KEY (id_player) REFERENCES players(id)
);

-- insert into games (name_player, score, id_player)values
-- ("Ivan", 2200, 1),
-- ("Ivan", 2600, 1),
-- ("Ivan", 2500, 1),
-- ("Irakli", 100, 2),
-- ("Irakli", 50, 2),
-- ("Masha", 550, 3);


select * from games;
select * from games, players where games.id_player = players.id;





-- drop database if exists test;