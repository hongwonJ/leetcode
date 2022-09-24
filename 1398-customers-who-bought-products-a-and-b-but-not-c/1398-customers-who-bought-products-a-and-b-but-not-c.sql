# Write your MySQL query statement below
SELECT c.customer_id, customer_name
FROM Customers c LEFT JOIN Orders o ON c.customer_id = o.customer_id
WHERE c.customer_id IN (
    SELECT customer_id FROM Orders WHERE product_name = 'A'
) AND c.customer_id IN (
    SELECT customer_id FROM Orders WHERE product_name = 'B'
) AND c.customer_id NOT IN (
    SELECT customer_id FROM Orders WHERE product_name = 'C'
)
GROUP BY c.customer_id

