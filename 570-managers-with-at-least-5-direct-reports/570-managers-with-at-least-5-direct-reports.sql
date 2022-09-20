# Write your MySQL query statement below

SELECT name
FROM Employee E JOIN (
    SELECT managerId, COUNT(*) AS manager_count
    FROM Employee
    GROUP BY managerId
) AS Nums
    ON E.id = Nums.managerId
WHERE Nums.manager_count + IF(E.managerId IS NULL, 1, 0) >= 5
