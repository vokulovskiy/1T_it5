create table if not exists users (
    id serial primary key,
    name varchar(100),
    age int
);

insert into users (name, age) values
('Ivan', 29),
('Dmitry', 27),
('Maxim', 19);