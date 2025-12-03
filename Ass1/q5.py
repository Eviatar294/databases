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
        """
    )
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()