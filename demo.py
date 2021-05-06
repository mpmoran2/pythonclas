import psycopg2

#  connect to a database. go to psql and get the info you need
conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")
cur = conn.cursor()
# once cursor is created, to create a table
cur.execute('''CREATE TABLE demo(ID serial, Name text, Color text, Age int);''')
print("Table Created")
# to save it
conn.commit()
conn.close()

