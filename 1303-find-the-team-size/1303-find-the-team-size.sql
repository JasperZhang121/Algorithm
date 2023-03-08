# Write your MySQL query statement below

with temp as(select team_id, count(team_id) as team_size from employee group by team_id)

select employee_id, team_size from employee natural join temp; 
