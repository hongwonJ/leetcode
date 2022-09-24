# Write your MySQL query statement below

SELECT E.employee_id FROM Employees E LEFT JOIN Salaries S ON E.employee_id = S.employee_id 
WHERE ISNULL(salary)
UNION
SELECT S.employee_id FROM Salaries S LEFT JOIN Employees E ON E.employee_id = S.employee_id 
WHERE ISNULL(name)
ORDER BY employee_id ASC