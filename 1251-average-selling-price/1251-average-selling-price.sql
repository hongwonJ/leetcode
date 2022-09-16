# Write your MySQL query statement below

SELECT us.product_id, ROUND(SUM(price*units)/SUM(units), 2) AS average_price
FROM UnitsSold AS us LEFT JOIN Prices AS p
    ON us.product_id = p.product_id
WHERE start_date <= purchase_date 
    AND purchase_date <= end_date
GROUP BY product_id

