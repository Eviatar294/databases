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
        WITH num_victories_1999 as (
	SELECT Car, COUNT(*) as num_victories
    FROM winners as w
    WHERE YEAR(w.date) = 1999
    GROUP BY w.car
),
gloriest_car_1999 as (
	SELECT Car
    FROM num_victories_1999
    ORDER BY num_victories DESC
    LIMIT 1
)
SELECT COUNT(*)
FROM winners w
JOIN gloriest_car_1999 g ON w.Car = g.Car
WHERE YEAR(w.date) = 2001
        """
    )
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()