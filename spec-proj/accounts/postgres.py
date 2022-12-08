import psycopg2

# Update connection string information

host = 'dbspectionserver.postgres.database.azure.com'
dbname = 'dbspectionserver'
user = 'spectionadmin@dbspectionserver'
password = 'Minions1'
sslmode = 'require'

# Construct connection string

conn_string= dbname='dbspection' user='spectionadmin@dbspectionserver' host='dbspectionserver.postgres.database.azure.com' password='Minions1' port='5432' sslmode='true'
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()
