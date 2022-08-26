# Write your MySQL query statement below

Update Salary
SET sex =
CASE
    WHEN sex ='f' THEN 'm'
    ELSE 'f'
END;