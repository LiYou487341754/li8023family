import random
from tkinter import *
from tkinter import ttk
from pymysql import connect


def frist_page():
    global page
    if page != frame1:
        page.pack_forget()  # 取消显示当前界面，并不是销毁
        page = frame1
        page.pack()  # 显示界面1


def second_page():
    global page
    if page != frame2:
        page.pack_forget()  # 取消显示当前界面，并不是销毁
        page = frame2
        page.pack()  # 显示界面2
        data = response()
        figure = j_figure()
        w_mean = data[figure[j]][0]
        label5.configure(text=w_mean)


def three_page():
    global page
    if page != frame3:
        page.pack_forget()  # 取消显示当前界面，并不是销毁
        page = frame3
        page.pack()  # 显示界面3
        data = response()
        figures = i_figures()
        c_mean = data[figures[i]][1]
        label12.configure(text=c_mean)


def i_figures():
    i_sequence = sequence()
    return i_sequence


def j_figure():
    j_sequence = sequence()
    return j_sequence


def sequence():
    data = response()
    sequences = range(len(data))
    random_sequence = random.sample(sequences, len(data))
    return random_sequence


def response():
    conn = connect(host='localhost', user='root', password='LIyou6976', database='words',
                   port=3306, charset="utf8")
    cur = conn.cursor()
    cur.execute("select *from word")
    data = cur.fetchall()
    return data


def e_c_next():
    global j
    root.update()
    data = response()
    if len(data) - 1 > j:
        j += 1
        figure = j_figure()
        c_mean = data[figure[j]][0]
        label5.configure(text=c_mean)


def c_e_next():
    global i
    root.update()
    data = response()
    if len(data)-1 > i:
        i += 1
        root.update()
        figures = i_figures()
        c_mean = data[figures[i]][1]
        label12.configure(text=c_mean)


def write_in():  # 写入文件
    try:
        conn = connect(host='localhost', user='root', password='LIyou6976', database='words', port=3306,
                       charset="utf8")
        cur = conn.cursor()
        cur.execute("insert into word(word, translate)values(%s,%s)", (entry1.get(), entry2.get()))
        conn.commit()
        if entry1.get() not in response() and len(entry1.get()) != 0:
            label3 = ttk.Label(frame6, text="写入成功" + "   " + entry1.get() + "   :  " + entry2.get(), font=("华文新魏", 13),
                               foreground='red')
            label3.grid(row=0, column=0, pady=20)
            root.update()
        elif len(entry1.get()) != 0:
            label3 = ttk.Label(frame6, text="单词已经记录", font=("华文新魏", 13), foreground='red')
            label3.grid(row=0, column=0, pady=20)
            root.update()

    except Exception as e:
        root.update()
        e = str(e)
        label4 = ttk.Label(frame6, text=e, font=("华文新魏", 13))
        label4.grid(row=1, column=0,  pady=20)


def e_c_translation():
    root.update()
    data = response()
    figure = j_figure()
    e_c_word = data[figure[j]][1]
    if entry3.get() == e_c_word:
        label7 = ttk.Label(frame9, text="正确", font=("华文新魏", 13), foreground='red')
        label7.grid(row=1, column=1, padx=5, pady=20)
    else:
        label8 = ttk.Label(frame9, text='错误', font=("华文新魏", 13), foreground='red')
        label8.grid(row=1, column=1, padx=5, pady=20)


def c_e_translation():
    root.update()
    data = response()
    figures = i_figures()
    c_e_word = data[figures[i]][0]
    if entry4.get() == c_e_word:
        label15 = ttk.Label(frame12, text='正确', font=("华文新魏", 13), foreground='red')
        label15.grid(row=1, column=1, padx=5, pady=20)
    else:
        label16 = ttk.Label(frame12, text='错误', font=("华文新魏", 13), foreground='red')
        label16.grid(row=1, column=1, padx=5, pady=20)


def clear_word():
    entry1.delete(0, "end")


def clear_translate():
    entry2.delete(0, 'end')


def clear_all():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')


root = Tk()
root.title('英语单词听写器')
root.geometry("650x300+300+200")
root.resizable(True, True)
# 模式选择
style1 = ttk.Style()
style1.configure("TButton", font=("华文行楷", 13))
frame0 = ttk.Frame(root, height=30, width=500)
frame0.pack(side='top')
button1 = ttk.Button(frame0, text="记录", command=frist_page)
button2 = ttk.Button(frame0, text="英译汉", command=second_page)
button3 = ttk.Button(frame0, text="汉译英", command=three_page)
button1.pack(side='left', ipadx=10)
button2.pack(side='left', ipadx=10, expand=True)
button3.pack(side="right", ipadx=10)
frame1 = ttk.Frame(root, height=30, width=500)
frame2 = ttk.Frame(root, height=30, width=500)
frame3 = ttk.Frame(root, height=30, width=500)
# 界面一
frame4 = ttk.Frame(frame1, height=30, width=500)
frame5 = ttk.Frame(frame1, height=30, width=500)
frame6 = ttk.Frame(frame1, height=30, width=500)
# 界面一控件
label1 = ttk.Label(frame4, text="英语单词:", font=("华文新魏", 13))
word = StringVar()
mean = StringVar()
entry1 = ttk.Entry(frame4, textvariable=word, font=("华文新魏", 13), width=18)
label2 = ttk.Label(frame4, text="英语翻译:", font=("华文新魏", 13))
entry2 = ttk.Entry(frame4, textvariable=mean, font=("华文新魏", 13), width=18)
style2 = ttk.Style()
style2.configure("TButton", font=("华文新魏", 13))
button4 = ttk.Button(frame4, text="写入", width=10, command=write_in)
button5 = ttk.Button(frame5, text="单词清空", command=clear_word)
button6 = ttk.Button(frame5, text="翻译清空", command=clear_translate)
button7 = ttk.Button(frame5, text="全部清空", command=clear_all)
# 布局
frame4.pack()
frame5.pack()
frame6.pack()
label1.grid(row=2, column=0, padx=1, pady=20)
entry1.grid(row=2, column=1, padx=1, pady=20)
label2.grid(row=2, column=2, padx=1, pady=20)
entry2.grid(row=2, column=3, padx=1, pady=20)
button4.grid(row=2, column=4, padx=1, pady=20)
button5.grid(row=3, column=0, padx=20, pady=20)
button6.grid(row=3, column=1, padx=20, pady=20)
button7.grid(row=3, column=2, padx=20, pady=20)
page = frame1
page.pack()
# 界面二
frame7 = ttk.Frame(frame2, height=30, width=500)
frame8 = ttk.Frame(frame7, height=30, width=500)
frame9 = ttk.Frame(frame2, height=30, width=500)
# 界面二控件
label5 = ttk.Label(frame8, text='', font=("华文新魏", 25), foreground='red')
label6 = ttk.Label(frame9, text="英译汉:", font=("华文新魏", 13))
e_c_translate = StringVar()
entry3 = ttk.Entry(frame9, textvariable=e_c_translate, font=("华文新魏", 13))
style3 = ttk.Style()
style3.configure("TButton", font=("华文新魏", 13))
button8 = ttk.Button(frame9, text='确认', command=e_c_translation)
label9 = ttk.Label(frame9, text="正确与否:", font=("华文新魏", 13))
button9 = ttk.Button(frame9, text="下一个", command=e_c_next)
# 界面二布局
frame7.pack()
frame8.pack()
frame9.pack()
label5.grid(row=0, column=0, pady=20)
label6.grid(row=0, column=0, padx=5, pady=20)
entry3.grid(row=0, column=1, padx=1, pady=20)
button8.grid(row=0, column=2, padx=1, pady=20)
label9.grid(row=1, column=0, padx=5, pady=20)
button9.grid(row=1, column=2, padx=5, pady=20)
# 界面三
frame10 = ttk.Frame(frame3, height=30, width=500)
frame11 = ttk.Frame(frame10, height=30, width=500)
frame12 = ttk.Frame(frame3, height=30, width=500)
# 界面三控件
label12 = ttk.Label(frame11, text='', font=("华文新魏", 25), foreground='red')
label13 = ttk.Label(frame12, text="汉译英", font=("华文新魏", 13))
c_e_translate = StringVar()
entry4 = ttk.Entry(frame12, textvariable=c_e_translate, font=("华文新魏", 13))
style4 = ttk.Style()
style4.configure("TButton", font=("华文新魏", 13))
button10 = ttk.Button(frame12, text="确认", command=c_e_translation)
label14 = ttk.Label(frame12, text="正确与否:", font=("华文新魏", 13))
button11 = ttk.Button(frame12, text="下一个", command=c_e_next)
# 界面三布局
frame10.pack()
frame11.pack()
frame12.pack()
label12.grid(row=0, column=0, pady=20)
label13.grid(row=0, column=0, padx=5, pady=20)
entry4.grid(row=0, column=1, padx=1, pady=20)
button10.grid(row=0, column=2, padx=1, pady=20)
label14.grid(row=1, column=0, padx=5, pady=20)
button11.grid(row=1, column=2, padx=5, pady=20)
i = 0
j = 0
root.mainloop()
