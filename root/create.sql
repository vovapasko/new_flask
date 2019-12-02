create Table player(
	player_id int NOT NULL,
	balance int NOT NULL,
	passwrd varchar(64) NOT NULL
);
alter table player add constraint player_id_pk PRIMARY KEY(player_id);

create table usernames(
	player_id int NOT NULL,
	player_name VARCHAR(40),
	play_surname VARCHAR(40),
	player_nickname VARCHAR(40) NOT NULL
);
alter table usernames add constraint player_id_pk1 PRIMARY KEY(player_id);
alter table usernames add constraint player_id_fk FOREIGN KEY(player_id)
REFERENCES player(player_id);


create Table bet(
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
alter table casino add constrain  t player_fk FOREIGN KEY (player_id) REFERENCES player(player_id);
alter table casino add constraint bet_fk FOREIGN KEY (bet_id) REFERENCES bet(bet_id);

create table bank(
	player_id int NOT NULL,
	sold_time timestamp NOT NULL,
	sold_coins float NOT NULL
);
alter table bank add constraint p_id_time_pk PRIMARY KEY(player_id, sold_time);
alter table bank add constraint id_player_fk FOREIGN KEY(player_id) REFERENCES player(player_id);



create table countries(
	country_name varchar(255) NOT NULL,
	country_capital varchar(255) NOT NULL,
	country_population int NOT NULL,
	country_square float NOT NULL
);
alter table countries add constraint country_id_pk PRIMARY KEY(country_name);
