-- Write your PostgreSQL query statement below
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date >= DATE '2019-07-27' - 29 and activity_date <= DATE '2019-07-27'
GROUP BY activity_date
HAVING COUNT(DISTINCT user_id) >= 1
ORDER BY activity_date;