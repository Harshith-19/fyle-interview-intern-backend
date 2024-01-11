-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT teacher_id, COUNT(*) AS max_graded_count FROM assignments WHERE grade = 'A' GROUP BY teacher_id ORDER BY max_graded_count DESC LIMIT 1;
