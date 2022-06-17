# Write your MySQL query statement below
SELECT RES.customer_number
FROM (
    SELECT customer_number ,count(order_number) as counter
    FROM Orders
    GROUP BY customer_number
    ORDER BY counter desc
    LIMIT 1    
    ) as RES

