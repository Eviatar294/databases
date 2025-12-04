import mysql.connector
if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port="3307",
    )

    cursor = mydb.cursor()
    cursor.execute("""
        WITH laps_2000 AS (
    SELECT 
        w.`Name Code` AS code,
        SUM(w.`Laps`) AS total_laps
    FROM winners w
    WHERE YEAR(w.`Date`) = 2000
    GROUP BY w.`Name Code`
),
top_driver AS (
    SELECT code
    FROM laps_2000
    WHERE total_laps = (SELECT MAX(total_laps) FROM laps_2000)
)
SELECT 
    d.`Driver` AS driver,
    MIN(f.`Time`) AS min_time
FROM top_driver td
JOIN drivers_updated d 
    ON d.`Code` = td.code AND d.`Year` = 2000
JOIN fastest_laps_updated f 
    ON f.`Code` = td.code AND f.`Year` = 2000
GROUP BY d.`Driver`;

        """
    )
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()