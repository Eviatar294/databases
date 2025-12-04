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
    # Union selects unique values from both sets:
    # 1. Winners driving Ferrari
    # 2. Drivers with ARG nationality
    SELECT Winner AS driver FROM winners WHERE Car = 'Ferrari'
    UNION
    SELECT Driver AS driver FROM drivers_updated WHERE Nationality = 'ARG'
    ORDER BY driver ASC;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()