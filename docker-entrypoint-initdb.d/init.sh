set -e
psql -U postgres << EOSQL
create database project;
EOSQL