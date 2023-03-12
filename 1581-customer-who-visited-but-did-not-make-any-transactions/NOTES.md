where statement will always before select, as a result

`where visit_id not in (select visit_id from transactions) ` -> all id that not in transactions but in table visit 

`select customer_id, count(visit_id) as count_no_trans from visits` -> count the temp table after where statement
