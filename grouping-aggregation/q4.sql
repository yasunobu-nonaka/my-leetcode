SELECT results
 FROM (
    SELECT u.name AS results
    FROM MovieRating mr
    LEFT JOIN Users u
        ON u.user_id = mr.user_id
    GROUP BY mr.user_id, u.name
    ORDER BY COUNT(mr.rating) DESC, u.name
    LIMIT 1
) t1

UNION ALL

SELECT results
FROM (
    SELECT mo.title AS results
    FROM MovieRating mr
    LEFT JOIN Movies mo
        ON mo.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01' AND mr.created_at < '2020-03-01'
    GROUP BY mr.movie_id, mo.title
    ORDER BY AVG(mr.rating) DESC, mo.title
    LIMIT 1
) t2;