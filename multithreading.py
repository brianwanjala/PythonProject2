import pymysql
#establish connection
connection = pymysql.connect(host="localhost",
                          user = "root",
                          password = "@Njoroschool22",
                          database= "testdb"   )

try:
    #create a cursor
    cursor = connection.cursor()
    print("Connection successful")

    #Connect to database
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print(f"Connected to database {db_name}")

except pymysql.MySQLError as e:
    print(f"Failed to connect to Mysql! {e}")

finally:
    if connection:
        connection.close()
        print("Connection closed")

