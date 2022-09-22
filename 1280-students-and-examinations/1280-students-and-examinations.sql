# Write your MySQL query statement below

SELECT S.*, SB.*, IF(nums IS NULL, 0, nums) AS attended_exams
FROM Students AS S
    JOIN Subjects AS SB
    LEFT JOIN (
        SELECT student_id, subject_name, COUNT(*) AS nums
        FROM Examinations
        GROUP BY student_id, subject_name
    ) AS EX
    ON S.student_id = EX.student_id AND SB.subject_name = EX.subject_name
ORDER BY S.student_id, SB.subject_name
    