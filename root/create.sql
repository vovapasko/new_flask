Create Table player(
	player_id int NOT NULL,
	balance int NOT NULL,
	passwrd varchar(64) NOT NULL
);
ALTER TABLE player add constraint player_id_pk PRIMARY KEY(player_id);

create table usernames(
	player_id int NOT NULL,
	player_name VARCHAR(40),
	play_surname VARCHAR(40),
	player_nickname VARCHAR(40) NOT NULL
);
ALTER TABLE usernames add constraint player_id_pk1 PRIMARY KEY(player_id);
--ALTER TABLE usernames add constraint player_id_fk FOREIGN KEY(player_id)
REFERENCES player(player_id);


Create Table bet(
	bet_id int NOT NULL,
	bet_money float NOT NULL,
	won_money float NOT NULL,
	won_bet boolean NOT NULL,
	bet_time timestamp NOT NULL
);
alter table bet add constraint bet_id_pk PRIMARY KEY(bet_id);

create table casino(
	player_id int NOT NULL,
	bet_id int NOT NULL
);
alter table casino add constraint player_bet_id_pk PRIMARY KEY(player_id, bet_id);
--alter table casino add constrain  t player_fk FOREIGN KEY (player_id) REFERENCES player(player_id);
--alter table casino add constraint bet_fk FOREIGN KEY (bet_id) REFERENCES bet(bet_id);

CREATE table bank(
	player_id int NOT NULL,
	sold_time timestamp NOT NULL,
	sold_coins float NOT NULL
);
alter table bank add constraint p_id_time_pk PRIMARY KEY(player_id, sold_time);
--alter table bank add constraint id_player_fk FOREIGN KEY(player_id) REFERENCES player(player_id);
