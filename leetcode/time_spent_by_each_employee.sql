SELECT event_day as day, emp_id, SUM(time_diff) as total_time FROM (SELECT *, (out_time - 
in_time) as time_diff FROM employees) my_table GROUP BY emp_id, event_day
