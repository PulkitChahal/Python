create database sql_pwskills;

use sql_pwskills;

-- DDL Commands - create, drop, insert, truncate

CREATE TABLE IF NOT EXISTS pwstudents (
    studentid INT,
    student_name CHAR(50),
    student_email VARCHAR(100),
    joining_date DATE,
    short_desc TEXT,
    marks DECIMAL(3, 2) -- 000.00
);

select * from pwstudents;

describe pwstudents;

-- drop table pwstudents;

-- drop database pw_skills;

alter table pwstudents add column weight float;
-- OR 
alter table pwstudents add weight float;

alter table pwstudents drop column short_desc;
-- OR
alter table pwstudents drop short_desc;

alter table pwstudents modify column weight int;
-- OR
alter table pwstudents modify weight int;

alter table pwstudents rename column weight to mass;
-- OR
-- alter table pwstudents rename weight to mass;

describe pwstudents;  

select * from pwstudents;

insert into pwstudents value (1, 'deepak', 'deepak123@gmail.com', '2023-11-11', 8.4, 67);

select * from pwstudents;

truncate pwstudents;
-- OR
truncate table pwstudents;
 
select * from pwstudents;

-- drop table pwstudents;

