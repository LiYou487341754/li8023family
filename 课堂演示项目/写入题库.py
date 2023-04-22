import sqlite3

con = sqlite3.connect('./sign.db')
cur = con.cursor()

sql = 'insert into question_bank(subject, option_A,  option_B,  option_C,  option_D, answer) values(?,?,?,?,?,?)'
subject = input('请输入题目:')
option_A = input('请输入选项A:')
option_B = input('请输入选项B:')
option_C = input('请输入选项C:')
option_D = input('请输入选项D:')
answer = input('请输入答案:')

try:

    cur.execute(sql, (subject, option_A, option_B, option_C, option_D, answer))
    con.commit()
    print("录入成功")
except Exception as e:
    print(e)
    con.rollback()
    print("录入失败")

finally:
    cur.close()
    con.close()
