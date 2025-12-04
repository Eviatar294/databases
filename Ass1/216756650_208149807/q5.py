import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port="3307",
    )
    cursor = mydb.cursor()
    cursor.execute("""
    # Calculate average points from teams_updated.
    # Filter only for cars present in fastest_laps_updated with time < 2 minutes.
    # Use the MINUTE() hint provided in the assignment.
    SELECT t.Car, AVG(t.PTS) AS avg_pts
    FROM teams_updated t
    WHERE t.Car IN (
        SELECT DISTINCT Car
        FROM fastest_laps_updated
        WHERE MINUTE(STR_TO_DATE(Time, '%i:%s.%f')) < 2
    )
    GROUP BY t.Car
    ORDER BY avg_pts DESC;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()