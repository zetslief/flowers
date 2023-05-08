import psycopg2
import csv

conn_params = {
    "host": "localhost",
    "database": "flowers",
    "user": "postgres",
    "password": "root"
}

conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

with open("db.sql", "r") as f:
    cur.execute(f.read())

cur.execute("DELETE FROM flower")

with open('flower_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader) 
    with conn.cursor() as cur:
        for row in reader:
            name, image_url = row
            cur.execute("INSERT INTO flower (name, image_url) VALUES (%s, %s)", (name, image_url))
        conn.commit()

cur.close()
conn.close()
