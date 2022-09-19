# Write your MySQL query statement below
SELECT left_operand, operator, right_operand, (
    CASE 
    WHEN operator = '>' THEN IF(v1.value > v2.value, 'true', 'false')
    WHEN operator = '<' THEN IF(v1.value < v2.value, 'true', 'false')
    ELSE IF(v1.value = v2.value, 'true', 'false')
    END) as value
FROM Expressions e JOIN Variables v1
    ON e.left_operand = v1.name
    JOIN Variables v2 
    ON e.right_operand = v2.name