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
        """
    )
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()