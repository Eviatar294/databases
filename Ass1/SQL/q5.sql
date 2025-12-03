WITH fastest_leap_b_2m as (
	SELECT DISTINCT f.Car
    FROM fastest_laps_updated f
    WHERE MINUTE(STR_TO_DATE(f.Time, '%i:%s.%f')) < 2
)
SELECT t.Car, AVG(t.PTS) as avg_pts
FROM teams_updated t
JOIN fastest_leap_b_2m f ON t.Car = f.Car
GROUP BY t.Car
ORDER BY avg_pts DESC