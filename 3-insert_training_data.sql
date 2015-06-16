create table training_data (label smallint, val smallint[]);
copy training_data from '/home/gpadmin/demo2/1-psql_loadable.txt' DELIMITER '|' CSV;

