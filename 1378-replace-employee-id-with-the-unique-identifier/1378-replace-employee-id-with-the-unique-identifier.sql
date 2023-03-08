# Write your MySQL query statement below

select unique_id,name from employeeuni eu

    right join employees as ep

        on eu.id = ep.id;
    
