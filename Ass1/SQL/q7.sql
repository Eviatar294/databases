SELECT DISTINCT d.Driver AS driver
FROM drivers_updated d
LEFT JOIN winners w
    ON d.Driver = w.Winner
WHERE d.Nationality = 'ARG'
   OR (d.Car = 'Ferrari' AND w.Winner IS NOT NULL)
ORDER BY driver ASC;