# Write your MySQL query statement below
SELECT R1.depname as Department, E.name as Employee, E.salary as Salary
FROM Employee E 
JOIN (SELECT D.id as depid, D.name as depname, max(E.salary) as salary
        FROM Employee as E JOIN Department D ON E.departmentId = D.id
        GROUP BY D.name) R1 
ON R1.depid = E.departmentId and E.salary = R1.salary