# Write your MySQL query statement below
SELECT MAX(num) AS num
From (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) as sq;

