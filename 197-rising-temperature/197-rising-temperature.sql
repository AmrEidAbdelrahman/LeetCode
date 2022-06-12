# Write your MySQL query statement below
SELECT RES.ID1 as Id
FROM
(SELECT W1.id as ID1, W1.recordDate as R1, W1.temperature as T1, W2.id as ID2, W2.recordDate as R2, W2.temperature as T2
FROM Weather W1, Weather W2
WHERE DATEDIFF(W1.recordDate, W2.recordDate) = 1
AND W1.temperature > W2.temperature) as RES

