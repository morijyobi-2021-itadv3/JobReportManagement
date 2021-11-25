set -e
psql -U admin << EOSQL
CREATE TABLE data(
   txt varchar(100) PRIMARY KEY
   );

insert into data values('Hello');
EOSQL
