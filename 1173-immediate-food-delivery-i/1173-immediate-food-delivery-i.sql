# Write your MySQL query statement below

SELECT ROUND(COUNT(immediate_orders.delivery_id) / COUNT(delivery.delivery_id) * 100, 2) AS immediate_percentage
FROM delivery
LEFT JOIN (
  SELECT delivery_id
  FROM delivery
  WHERE order_date = customer_pref_delivery_date
) AS immediate_orders ON delivery.delivery_id = immediate_orders.delivery_id;



