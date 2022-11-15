import mysql.connector;

data = [
    [12100477, 28, 'Govind', 'Krishna'],
    [12100435, 11, 'Suyash', 'Purwar'],
    [12193212, 19, 'Bhura', 'Singh'],
    [12300842, 34, 'Kalu', 'Mehta'],
    [11302341, 45, 'Tillu', 'Sarkar'],
    [12003423, 32, 'Vidhusi', 'Purwar']
]

try:
    dbcon = mysql.connector.connect(host='localhost', database='int213', user='root', password='AshNov06@')
    cursor = dbcon.cursor()

    create_table_query = "CREATE TABLE Students (reg_no int, roll_no int, first_name VARCHAR(255), last_name VARCHAR(255));"

    # cursor.execute(create_table_query)

    for record in data:
        insert_table_query_one = "INSERT INTO Students (reg_no, roll_no, first_name, last_name) VALUE (" + str(record[0]) + ", " + str(record[1]) + ", '" + record[2] + "', '" + record[3] + "');"
        cursor.execute(insert_table_query_one)
        dbcon.commit()

    # delete_table_row = "DELETE FROM Students WHERE roll_no = 11"

    dbcon.close()
except mysql.connector.Error as error:
    print(error)

