# Write your MySQL query statement below
SELECT S1.id, IF(NOT ISNULL(S2.student), S2.student, S1.student) AS student
FROM Seat S1 LEFT JOIN Seat S2
    ON IF(S1.id%2 = 1, S1.id = S2.id - 1, S1.id = S2.id + 1)
        