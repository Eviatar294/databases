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
        SELECT DISTINCT d.Driver AS driver
FROM drivers_updated d
LEFT JOIN winners w
    ON d.Driver = w.Winner
WHERE d.Nationality = 'ARG'
   OR (d.Car = 'Ferrari' AND w.Winner IS NOT NULL)
ORDER BY driver ASC;
        """
    )
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()