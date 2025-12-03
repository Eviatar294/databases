WITH num_victories_1999 as (
	SELECT Car, COUNT(*) as num_victories
    FROM winners as w
    WHERE YEAR(w.date) = 1999
    GROUP BY w.car
),
gloriest_car_1999 as (
	SELECT Car
    FROM num_victories_1999
    ORDER BY num_victories DESC
    LIMIT 1
)
SELECT COUNT(*)
FROM winners w
JOIN gloriest_car_1999 g ON w.Car = g.Car
WHERE YEAR(w.date) = 2001

