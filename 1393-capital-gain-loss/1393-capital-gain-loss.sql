# Write your MySQL query statement below
SELECT RES1.stock_name, RES2.gain_loss - RES1.gain_loss as capital_gain_loss
FROM (SELECT stock_name, sum(price) as gain_loss
      FROM Stocks
      WHERE operation = 'Buy'
      GROUP BY stock_name) as RES1 JOIN
      (SELECT stock_name, sum(price) as gain_loss
      FROM Stocks
      WHERE operation = 'Sell'
      GROUP BY stock_name) as RES2
      ON RES1.stock_name = RES2.stock_name
      
# SELECT stock_name, SUM(
#     CASE
#         WHEN operation = 'Buy' THEN -price
#         ELSE price
#     END
# ) AS capital_gain_loss
# FROM Stocks
# GROUP BY stock_name
