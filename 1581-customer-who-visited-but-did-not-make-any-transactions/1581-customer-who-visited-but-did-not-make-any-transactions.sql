# Write your MySQL query statement below
SELECT V.customer_id, count(V.visit_id) - count(T.visit_id) as count_no_trans
FROM Visits V LEFT JOIN Transactions T ON V.visit_id = T.visit_id
GROUP BY V.customer_id
HAVING count_no_trans != 0