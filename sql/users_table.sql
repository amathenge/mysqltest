-- MySQL users table

drop table if exists users;

create table users (
    id integer primary key auto_increment,
    firstname varchar(64) not null,
    lastname varchar(64) not null,
    phone varchar(32) not null,
    email varchar(64) not null,
    notes text
);

