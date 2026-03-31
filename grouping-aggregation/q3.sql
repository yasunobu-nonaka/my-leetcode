-- Write your PostgreSQL query statement below
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN p_id IN (SELECT id FROM Tree) AND id IN (SELECT p_id FROM Tree) THEN 'Inner'
        WHEN p_id IN (SELECT id FROM Tree) AND id NOT IN (SELECT p_id FROM Tree WHERE p_id IS NOT NULL) THEN 'Leaf'
    END AS type
FROM Tree;