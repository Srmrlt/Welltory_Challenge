SELECT users.*
FROM users
JOIN (
    SELECT heart_rates.user_id, AVG(heart_rates.heart_rate) AS avg_heart_rate
    FROM heart_rates
    WHERE heart_rates.timestamp >= :date_from AND heart_rates.timestamp <= :date_to
    GROUP BY heart_rates.user_id
) AS avg_heart_rate_subquery
ON users.id = avg_heart_rate_subquery.user_id
WHERE users.age > :min_age
  AND users.gender = :gender
  AND avg_heart_rate_subquery.avg_heart_rate > :min_avg_heart_rate;


SELECT heart_rates.*,
       EXTRACT(HOUR FROM heart_rates.timestamp) AS hour,
       AVG(heart_rates.heart_rate) AS avg_heart_rate_by_hour
FROM heart_rates
WHERE heart_rates.user_id = :user_id
  AND heart_rates.timestamp >= :date_from
  AND heart_rates.timestamp <= :date_to
GROUP BY EXTRACT(HOUR FROM heart_rates.timestamp)
ORDER BY AVG(heart_rates.heart_rate) DESC
LIMIT 10;