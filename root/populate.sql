insert into player(player_id, balance, passwrd)
values(100, 150000, 'zelensky-molodets');
insert into player(player_id, balance, passwrd)
values(250, 6500, 'poroshenko-molodets');
insert into player(player_id, balance, passwrd)
values(300, 13030, 'yanukovich-molodets');

insert into usernames(player_id, player_name, play_surname, player_nickname)
values(100, 'Vasya', 'Zopin', 'Zeva');
insert into usernames(player_id, player_name, play_surname, player_nickname)
values(250, 'Petya', NULL, 'Pi');
insert into usernames(player_id, player_name, play_surname, player_nickname)
values(300, NULL, 'Yano', 'Yn');

insert into bet(bet_id, bet_money, won_money, won_bet, bet_time)
values (1, 1500.34, 23400, false, '2016-06-22 19:10:25-07');
insert into bet(bet_id, bet_money, won_money, won_bet, bet_time)
values (2, 34200, 233145400, true, '2019-06-22 19:10:25-07');
insert into bet(bet_id, bet_money, won_money, won_bet, bet_time)
values (3, 1245004, 2312313400, true, '2018-06-22 19:10:25-07');

insert into casino(player_id, bet_id)
values(100, 1);
insert into casino(player_id, bet_id)
values(250, 2);
insert into casino(player_id, bet_id)
values(300, 3);

insert into bank(player_id, sold_time, sold_coins)
values(100, '2016-06-22 14:10:25-07', 3000);
insert into bank(player_id, sold_time, sold_coins)
values(250, '2018-06-22 14:10:25-07', 90000);
insert into bank(player_id, sold_time, sold_coins)
values(300, '2017-06-22 14:10:25-07', 3000000);