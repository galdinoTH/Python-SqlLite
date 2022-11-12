import sqlite3

#maximo de tabelas 2 bilhoes
#maximo de 2000 colunas
#maximo de registro(1.8e+19)(140GB)
#acesso para apenas um usuario

path = 'D:\Projects\python3\SqlLite'
conn = sqlite3.connect(path+r'\teste.db')
conn.close()