import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="16805", port=5432)

cur = conn.cursor()

# cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INT PRIMARY KEY,
#     name VARCHAR(255),
#     age INT,
#     gender CHAR
# );
# """)

# cur.execute("""
#     INSERT INTO person(id, name, age, gender) VALUES
#     (1, 'Mike', 30, 'm'),
#     (2, 'Lisa', 30, 'f'),
#     (3, 'Jhon', 54, 'm'),
#     (4, 'Bob', 80, 'm'),
#     (5, 'Julie', 40, 'f')
# """)

cur.execute("""SELECT * FROM person WHERE name='Bob';
""")
print(cur.fetchone())

cur.execute("""SELECT * FROM person WHERE age < 90;
""")

for row in cur.fetchone():
    print(row)

conn.commit()

cur.close()
conn.close()
