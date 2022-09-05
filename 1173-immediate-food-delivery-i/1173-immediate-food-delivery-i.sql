# Write your MySQL query statement below

SELECT ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0))*100/COUNT(*), 2) AS immediate_percentage
FROM Delivery