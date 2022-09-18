# Write your MySQL query statement below
SELECT seller_name
FROM Seller as s LEFT JOIN (
    SELECT sale_date, seller_id
    FROM Orders 
    WHERE YEAR(sale_date) = 2020
) as o2020 ON s.seller_id = o2020.seller_id
WHERE sale_date IS NULL
ORDER BY seller_name