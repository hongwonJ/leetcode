SELECT Email from (
    SELECT Email, COUNT(Email) as num
    FROM Person
    GROUP BY Email
) AS stats WHERE num > 1;
