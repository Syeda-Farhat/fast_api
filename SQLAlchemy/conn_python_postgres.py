import psycopg2
conn = psycopg2.connect(host="localhost", dbname = "postgres", user = "postgres", password="admin", port=5432)

cur = conn.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR);
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
            (1, 'Mike', 30, 'm'),
            (2, 'John', 35, 'm'),
            (3, 'Lisa', 33, 'f'),
            (4, 'Julia',34, 'f');

""")

conn.commit()

cur.close()
conn.close()