WITH sum_maserati as (
	SELECT SUM(t.PTS) as sumM
    FROM teams_updated t
    WHERE t.Car = "Maserati"
),
sum_ferrari as (
	SELECT SUM(t.PTS) as sumF
    FROM teams_updated t
    WHERE t.Car = "Ferrari"
)
SELECT f.sumf - m.sumM as "diff"
FROM sum_ferrari f, sum_maserati m