import postgresql

db = postgresql.open('pq://postgres:postgres@localhost:5432/mydb')
db.execute("CREATE TABLE msgs (msg CHAR(64))")