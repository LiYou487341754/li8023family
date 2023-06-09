import sqlite3

con = sqlite3.connect('./sign.db')
cur = con.cursor()

sql = '''
    create  table memorys(
    id int,
    digit_one varchar,
    digit_two varchar,
    username varchar,
    password varchar
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