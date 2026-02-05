create database Railways;
use Railways;

create table passengers(p_id int primary key,
book_id int,
first_name varchar(100) not null,
 last_name varchar(100),
 email varchar(50) unique not null,
 gender char(1));
 
insert ignore into passengers(p_id,
book_id,
first_name,
last_name ,
email,
gender)values(1,1,'Rajat','Sharma','rajat@gmail.com','M');
insert ignore into passengers(p_id,
book_id,
first_name,
last_name ,
email,
gender)values(2,2,'Mohit','kumar','mohit@gmail.com','M'),
(3,2,'Rajni','Singh','rajni@gmail.com','F');

 
select* from passengers;
 
 alter table passengers 
 add constraint booking_fk
 foreign key(book_id) references bookings(book_id);
 
 create table bookings(book_id int primary key,
 p_id int not null,
 t_id int not null,
 sourcee varchar(50),
 destination varchar(50),
 payment boolean);
 
 insert ignore into bookings(book_id,
 p_id ,
 t_id ,
 sourcee ,
 destination,
 payment) values(1,1,1,'Chandigarh','delhi',1);
 
 alter table bookings 
 add constraint train_fk
 foreign key(t_id) references trains(t_id);
 
 create table trains(t_id int primary key,
 t_name varchar(100),
 book_id int,
 p_id int);
 
 insert ignore into trains( t_id,
 t_name ,
 book_id,
 p_id) values (1,'Shatabdi',1,1);
 
 create table stations(st_id int primary key,
 sourcee varchar(50),
 destination varchar(50),
 stops varchar(50));
 
 insert into stations (st_id,
 sourcee ,
 destination,
 stops) values (1,'Chandigarh','Delhi',null);
 
 create table stops(stops_id int primary key,
 st_id int, stops varchar(50));
 
 insert into stops(stops_id ,
 st_id , stops) values(1,1,null);
 
 
 -- Queries
 
 select p.first_name,p.last_name,t.t_name, t.sourcee,t.destination from passengers p
 join trains on p.t_id =t.t_id;
 
 select t_name, count(*) from trains group by p_id;
 
 select first_name,last_name,count(t_id) from passengers group by t_id having count(t_id)>1;
 
 select t_name from trains where book_id is null;
 
 select t_name from trains where (select sum(p_id) from bookings);
 
 