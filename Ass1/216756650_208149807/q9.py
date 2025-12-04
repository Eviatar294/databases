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
        # CTE 1: Calculate the average points for each nationality
        WITH avg_pts_per_n AS (
            SELECT Nationality, AVG(PTS) AS avg_pts
            FROM drivers_updated
            GROUP BY Nationality
        ),
        # CTE 2: Find the minimum fastest lap time for each nationality
        min_lap_time_per_n AS (
            SELECT d.Nationality, MIN(f.Time) AS min_time
            FROM drivers_updated d
            JOIN fastest_laps_updated f 
                ON d.Driver = f.Driver
            GROUP BY d.Nationality
        ),
        # CTE 3: Find the most recent win date for each nationality
        recent_date_win_per_n AS (
            SELECT d.Nationality, MAX(w.Date) AS latest
            FROM drivers_updated d
            JOIN winners w 
                ON d.Driver = w.Winner
            GROUP BY d.Nationality
        )
        # Combine all metrics by joining the CTEs on Nationality
        # Use LEFT JOIN to ensure all nationalities from the average points list are included
        SELECT a.Nationality, a.avg_pts, m.min_time, r.latest
        FROM avg_pts_per_n a
        LEFT JOIN min_lap_time_per_n m ON a.Nationality = m.Nationality
        LEFT JOIN recent_date_win_per_n r ON a.Nationality = r.Nationality;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()