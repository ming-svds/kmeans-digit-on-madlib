create table test_data (label smallint, test_id smallint, val smallint[]);
copy test_data from '/home/gpadmin/demo/5-psql_loadable_test.txt' DELIMITER '|' CSV;
copy test_data from '/home/gpadmin/demo/1-test_label.txt' DELIMITER '|' CSV;

