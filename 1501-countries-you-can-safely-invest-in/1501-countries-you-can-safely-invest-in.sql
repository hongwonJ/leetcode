# Write your MySQL query statement below

SELECT name AS country
FROM (
    SELECT C.name, (SUM(Cs.duration)/ COUNT(Cs.duration)) AS avg_call
    FROM Country C
    LEFT JOIN Person P
    ON C.country_code = LEFT(P.phone_number, 3)
    LEFT JOIN Calls Cs
    ON P.id = Cs.caller_id OR P.id = Cs.callee_id
    WHERE Cs.duration IS NOT NULL
    GROUP BY C.name) AS call_stat
WHERE avg_call > (
    SELECT (SUM(Cs.duration)/ COUNT(Cs.duration))
    FROM Country C
    LEFT JOIN Person P
    ON C.country_code = LEFT(P.phone_number, 3)
    LEFT JOIN Calls Cs
    ON P.id = Cs.caller_id OR P.id = Cs.callee_id
    WHERE Cs.duration IS NOT NULL )

