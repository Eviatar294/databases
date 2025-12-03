WITH avg_points as (
	SELECT AVG(PTS)
    FROM drivers_updated d
)

SELECT d.Nationality, 
FROM drivers_updated d, nationalities n

GROUP BY d.Nationality