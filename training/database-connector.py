import mysql.connector

connector = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", passwd="root", database="python")

cursor = connector.cursor()

email = input("Email address: ")
password = input("Password: ")

insert_sql = "INSERT INTO user (email, password) VALUES ('{}', '{}')".format(email, password)
cursor.execute(insert_sql)
connector.commit()

select_sql = "SELECT * FROM user"
cursor.execute(select_sql)

result = cursor.fetchall()
print(["ID: {} | Email: {} | Password: {}".format(row[0], row[1], row[2]) for row in result])

connector.close()
