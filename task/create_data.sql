-- Вставка рандомных данных о пользователях
INSERT INTO users (name, gender, age)
SELECT 
    'User ' || g,
    CASE WHEN (random() < 0.5) THEN 'Male' ELSE 'Female' END,
    floor(random() * (80-18) + 18)::INTEGER
FROM generate_series(1, 50) g;

DO $$
DECLARE
    user_id INT;
    num_records INT;
BEGIN
    FOR user_id IN SELECT id FROM users LOOP
        num_records := floor(random() * 21 + 10)::INT; -- Генерация случайного количества записей от 10 до 30
        INSERT INTO heart_rates (user_id, timestamp, heart_rate)
        SELECT
            user_id,
            timestamp '2023-01-01 00:00:00' + (random() * (365 * 24) * interval '1 hour'), -- Случайная дата и время в пределах года
            floor(random() * (190-50) + 50)::INTEGER -- Случайное значение пульса от 50 до 190
        FROM generate_series(1, num_records);
    END LOOP;
END $$;
