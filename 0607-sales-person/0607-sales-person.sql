# Write your MySQL query statement below

SELECT name FROM SalesPerson 
WHERE sales_id not in
(select sales_id FROM Orders
where com_id=(select com_id from Company where name ='RED'));