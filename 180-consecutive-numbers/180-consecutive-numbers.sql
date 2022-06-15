# Write your MySQL query statement below
SELECT distinct(L1.num) as ConsecutiveNums
FROM Logs L1
JOIN Logs L2 ON L2.id = L1.id - 1 AND L2.num = L1.num
JOIN Logs L3 ON L3.id = L1.id + 1 AND L3.num = L1.num 
# JOIN Logs L4 ON L4.id = L1.id + 2 AND L4.num <> L1.num