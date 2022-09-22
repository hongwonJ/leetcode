# Write your MySQL query statement below

SELECT C.name AS country
FROM Country C
    LEFT JOIN Person ON country_code = LEFT(phone_number, 3)
    LEFT JOIN Calls ON id IN (caller_id, callee_id)
GROUP BY C.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM Calls)