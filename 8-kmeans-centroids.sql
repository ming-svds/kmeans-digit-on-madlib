-- Find 10 centroids from training table val column using dist_norm2 and average for aggregate function
\x auto;

select centroids from madlib.kmeanspp('training_data', 'val', 10, 'madlib.squared_dist_norm2', 'madlib.avg');
