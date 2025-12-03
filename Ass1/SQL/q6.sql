WITH gp_laps AS (
    SELECT DISTINCT
        `Grand Prix` AS GP,
        Laps
    FROM winners
    WHERE Laps >= 80
)
SELECT
    g1.GP AS GP1,
    g2.GP AS GP2,
    g1.Laps AS Laps
FROM gp_laps g1
JOIN gp_laps g2
    ON g1.Laps = g2.Laps      
   AND g1.GP < g2.GP         
ORDER BY
    Laps,
    GP1,
    GP2;