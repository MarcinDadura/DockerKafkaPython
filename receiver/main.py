from kafka import KafkaConsumer
from time import sleep
import mysql.connector
sleep(20)
try:
    connect = mysql.connector.connect(
        host="database",
        user="dockerdb",
        password="root",
        auth_plugin='mysql_native_password',
        database="temperatura")
     
except mysql.connector.Error as e:
    print("Error with database!")
consumer = KafkaConsumer('temp', bootstrap_servers=['broker:9092'])
tmp = 0
sum = 0
value = 0
for message in consumer:
    cursor = connect.cursor()
    tmp += 1
    value = int(message.value)
    sum += value
    print(str(value) + " wartosc otrzymana")
    if tmp == 10:
        tmp = 0
        sum = sum/10
        print(str(sum) + " srednia")
        cursor.execute("INSERT INTO temperatura.data(temperature, date_with_time) VALUES ( %s, CURRENT_TIMESTAMP())", (sum,))
        connect.commit()
        sum = 0
        cursor.close()
connect.close()

