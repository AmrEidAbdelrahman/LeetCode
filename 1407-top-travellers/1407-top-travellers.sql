# Write your MySQL query statement below
# SELECT U.name, CASE WHEN SUM(R.distance) IS NULL THEN 0 ELSE SUM(R.distance) END as travelled_distance
SELECT U.name, ifnull(SUM(R.distance),0) as travelled_distance
FROM Users U LEFT JOIN Rides R On U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance desc, U.name asc