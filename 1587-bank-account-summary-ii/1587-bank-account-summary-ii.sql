# Write your MySQL query statement below

select name, sum(amount) as balance from users

natural join transactions 

group by account

having balance>10000



