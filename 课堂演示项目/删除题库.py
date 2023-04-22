import sqlite3

con = sqlite3.connect('./sign.db')
cur = con.cursor()
sql = 'delete from question_bank where subject=?'
subject = input('请输入要删除的题目:')
try:
    cur.execute(sql, (subject,))
    con.commit()
    print('删除成功')

except Exception as e:
    print(e)
    print('删除失败')
finally:
    cur.close()
    con.close()
