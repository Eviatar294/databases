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
        # Calculate total laps for each driver (by Code) in wins from the year 2000
        WITH laps_2000 AS (
            SELECT 
                w.`Name Code` AS code,
                SUM(w.`Laps`) AS total_laps
            FROM winners w
            WHERE YEAR(w.`Date`) = 2000
            GROUP BY w.`Name Code`
        ),
        # Identify the driver code with the maximum total laps in 2000
        top_driver AS (
            SELECT code
            FROM laps_2000
            WHERE total_laps = (SELECT MAX(total_laps) FROM laps_2000)
        )
        # Retrieve Driver name and their minimum fastest lap time for the year 2000
        # Join drivers and fastest_laps tables using the code from the top_driver CTE
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