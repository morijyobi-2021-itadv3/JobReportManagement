create table sample(
    id serial,
    title text,
    primary key(id)
);

insert into sample (title) values ('テスト1');
insert into sample (title) values ('テスト2');
insert into sample (title) values ('テスト3');
