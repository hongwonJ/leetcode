# Write your MySQL query statement below


SELECT id, 
CASE
    WHEN p_id is NULL THEN 'Root'
    WHEN id NOT IN (
        SELECT DISTINCT p_id
        FROM Tree
        WHERE p_id IS NOT NULL
    ) THEN 'Leaf'
    ELSE 'Inner'
END as type
FROM Tree
ORDER BY id