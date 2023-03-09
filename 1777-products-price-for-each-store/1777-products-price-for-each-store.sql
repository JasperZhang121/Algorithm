# Write your MySQL query statement below

select product_id, 
sum(case when store="store1" then price end)"store1",
sum(case when store="store2" then price end)"store2",
sum(case when store="store3" then price end)"store3"
from products
group by product_id
