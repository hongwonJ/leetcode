SELECT email AS Email
FROM (SELECT email, COUNT(*) AS dups FROM Person GROUP BY email) AS nums
WHERE dups > 1