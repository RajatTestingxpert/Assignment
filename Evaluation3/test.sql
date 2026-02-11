create database emp;
use emp;

create table employee (emp_id int primary key ,name varchar(50),department char(2));

insert into employee(emp_id,name,department) values(1,"Ankit","IT"),
(2,"Priya","IT"),
(3,"Suman","HR"),
(4,"Rakesh","HR");

create table salaries(emp_id int primary key, salary int);

insert into salaries(emp_id,salary) values(1,80000),
(2,60000),
(3,50000),
(4,55000);

alter table salaries
add constraint fk_salaries
foreign key(emp_id) references employee(emp_id)
on update cascade
on delete cascade;

create table performance (emp_id int primary key,review_year int ,rating int);

insert into performance(emp_id,review_year,rating) values(1,2023,4),
(2,2024,5),
(3,2024,3),
(4,2024,4),
(5,2024,2);
alter table performance
add constraint fk_performance
foreign key(emp_id) references employee(emp_id);



select e.emp_id,e.name,avg(p.rating) from employee e join performance p where e.emp_id = p.emp_id group by e.emp_id;

select e.name,e.department,p.rating from employee e join performance p where e.emp_id = p.emp_id group by emp_id having salaries.salary >50000 ;

select e.name,e.department from employee e join performance p where e.emp_id= p.emp_id group by emp_id;