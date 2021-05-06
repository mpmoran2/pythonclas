import psycopg2

#  connect to a database. go to psql and get the info you need
conn = psycopg2.connect(dbname="postgres", user="postgres", password="2349", host="localhost", port="5432")

print("Database Connection Successful")