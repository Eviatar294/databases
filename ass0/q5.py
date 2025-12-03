import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="covid_db",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT date, location, new_cases
        FROM covid_deaths
        WHERE new_cases = weekly_hosp_admissions and new_cases != 0
        ORDER BY new_cases DESC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))