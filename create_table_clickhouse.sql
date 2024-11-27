CREATE TABLE users (
	id UInt32,
	name String,
	age UInt8
) ENGINE = MergeTree
ORDER BY id;


insert into users (id, name, age) values
(1, 'Denis', 16);
(2, 'Kate', 13),
(3, 'Ludmila', 52);