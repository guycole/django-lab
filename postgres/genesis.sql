--
--
--
create database mvp;
create user django with password 'awesome';
alter role django SET client_encoding TO 'utf8';
alter role django SET default_transaction_isolation TO 'read committed';
alter role django SET timezone TO 'UTC';
grant all privileges on database mvp to django;
--
--
