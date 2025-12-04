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
        # Filter for unique Grand Prix events with 80 or more laps
        WITH gp_laps AS (
            SELECT DISTINCT
                `Grand Prix` AS GP,
                Laps
            FROM winners
            WHERE Laps >= 80
        )
        # Self-join the filtered list to find pairs with the same lap count
        # Ensure GP1 comes before GP2 alphabetically to avoid duplicates (e.g., A-B vs B-A)
        SELECT
            g1.GP AS GP1,
            g2.GP AS GP2,
            g1.Laps AS Laps
        FROM gp_laps g1
        JOIN gp_laps g2
            ON g1.Laps = g2.Laps      
           AND g1.GP < g2.GP   
        """
    )
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()