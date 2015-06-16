

copy (select data.label, data.test_id, (madlib.closest_column(centroids, val)).column_id as cluster_id from test_data as data, (select centroids from madlib.kmeanspp('avg_2', 'val', 10, 'madlib.dist_norm2', 'madlib.avg', 100, 0.00001, 0.9)) as centroids order by data.label) to '/home/gpadmin/demo2/11-testout.txt';
