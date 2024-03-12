import sqlite3 as sql

con = sql.connect('form_db.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS  users')

sql = '''CREATE TABLE "discos" (
   "ID" INTEGER PRIMARY KEY AUTOINCREMENT,
   "ARTISTA" TEXT,
   "TITULO" TEXT,
   "ANO" TEXT,
   "GRAVADORA" TEXT
)'''

cur.execute(sql)
con.commit()
con.close()
