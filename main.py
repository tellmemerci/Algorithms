import psycopg2 as psycopg2

connection = psycopg2.connect(user="postgres", password="eurovision", host="localhost", port="5432",
                                          database="yandex")
print("База данных подключена")
cursor = connection.cursor()
insert_query = f"""SELECT * FROM POINTS;"""
cursor.execute(insert_query)
for row in cursor:
            print(row)