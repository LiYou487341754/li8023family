import sqlite3

con = sqlite3.connect('./sign.db')
cur = con.cursor()
sql = '''
    create  table question_bank(
    subject varchar,
    option varchar,
    answer varchar(20) not null
    )'''
try:
    cur.execute(sql)
    cur.close()
    con.close()
    print("创建成功")
except Exception as e:
    print(e)
    print('创建失败')
    cur.close()
    con.close()

