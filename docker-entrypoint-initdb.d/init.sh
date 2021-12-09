set -e
psql -U admin -d test << EOSQL
CREATE TABLE data(
   txt varchar(100) PRIMARY KEY
   );

insert into data values('Hello');
EOSQL
