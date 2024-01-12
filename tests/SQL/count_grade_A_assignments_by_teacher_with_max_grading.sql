-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) AS count
FROM assignments a1
JOIN (
    SELECT teacher_id
    FROM assignments
    GROUP BY teacher_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
) a2 ON a1.teacher_id = a2.teacher_id
WHERE a1.grade = 'A';
