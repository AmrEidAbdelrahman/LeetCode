CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT min(E1.salary)
      FROM (SELECT DISTINCT E2.salary 
            FROM Employee as E2
            # HAVING count(E2.salary) = N
            ORDER BY E2.salary desc 
            LIMIT N) as E1
      HAVING count(E1.salary) >= N and (N = 1 or min(E1.salary) != max(E1.salary))
  );
END