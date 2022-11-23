import webbrowser
from tkinter import *
import tkinter.ttk as ttk

urls = ['https://www.8090g.cn/jiexi/?url=', 'https://api.okjx.cc:3389/jx.php?url=', 'https://jx.aidouer.net/?url=',
        'https://2.08bk.com/?url=', 'https://z1.m1907.cn/?a=1&jx=', 'https://www.1717yun.com/api/?url=',
        'https://www.administratorw.com/admin.php?url=', 'https://jx.parwix.com:4433/player/?url=',
        'https://lecurl.cn/?url=', 'https://www.8090g.cn/?url=', 'https://jx.m3u8.tv/jiexi/?url=',
        'http://www.sfsft.com/video.php?url=']

zero = urls[0]
one = urls[1]
two = urls[2]
three = urls[3]
four = urls[4]
five = urls[5]
six = urls[6]
seven = urls[7]
eight = urls[8]
nine = urls[9]
ten = urls[10]
eleven = urls[11]

root = Tk()
root.title("vip视频解析")
root.geometry("400x300+%d+%d" % ((root.winfo_screenwidth()-400)/2, (root.winfo_screenheight()-300)/2))
root.iconbitmap('favicon.ico')
root.resizable(True, True)
root.attributes("-topmost", 0.5)
l1 = ttk.Label(root, text="播放接口:", font=("华文行楷", 12))
l1.grid(padx=10, pady=10)
l2 = ttk.Label(root, text="播放链接：", font=("华文行楷", 12))
l2.place(x=10, y=175)
ss = ttk.Style()
ss.configure("TEntry", borderwidth=4)
var0 = StringVar()
t1 = ttk.Entry(root, textvariable=var0, width=40, exportselection=False, style="TEntry")
t1.place(x=90, y=175)
var = StringVar()
var.set(zero)
sty = ttk.Style()
sty.configure('TRadiobutton', font=("华文行楷", 12))
r1 = ttk.Radiobutton(root, text='播放接口1', variable=var, value=zero, style='TRadiobutton')
r1.place(x=10, y=40)
r2 = ttk.Radiobutton(root, text='播放接口2', variable=var, value=one)
r2.place(x=280, y=40)
r3 = ttk.Radiobutton(root, text='播放接口3', variable=var, value=two)
r3.place(x=10, y=60)
r4 = ttk.Radiobutton(root, text='播放接口4', variable=var, value=three)
r4.place(x=280, y=60)
r5 = ttk.Radiobutton(root, text='播放接口5', variable=var, value=four)
r5.place(x=10, y=80)
r6 = ttk.Radiobutton(root, text='播放接口6', variable=var, value=five)
r6.place(x=280, y=80)
r7 = ttk.Radiobutton(root, text='播放接口7', variable=var, value=six)
r7.place(x=10, y=100)
r8 = ttk.Radiobutton(root, text='播放接口8', variable=var, value=seven)
r8.place(x=280, y=100)
r9 = ttk.Radiobutton(root, text='播放接口9', variable=var, value=eight)
r9.place(x=10, y=120)
r10 = ttk.Radiobutton(root, text='播放接口10', variable=var, value=nine)
r10.place(x=280, y=120)
r10 = ttk.Radiobutton(root, text='播放接口11', variable=var, value=ten)
r10.place(x=10, y=140)
r10 = ttk.Radiobutton(root, text='播放接口12', variable=var, value=eleven)
r10.place(x=280, y=140)


def bf():
    webbrowser.open(var.get()+t1.get())


s = ttk.Style()
s.configure('TButton', font=("华文行楷", 12), activebackgrond="yellow", releif="sunken")
b1 = ttk.Button(root, text="播放",  width=8, command=bf, style="TButton")
b1.place(x=10, y=200)


def del_text():
    t1.delete(0, 'end')


b2 = ttk.Button(root, text="清除", width=8, command=del_text, style="TButton")
b2.place(x=150, y=200)
b3 = ttk.Button(root, text="退出",  width=8, command=root.destroy, style="TButton")
b3.place(x=300, y=200)
root.resizable(False, False)
# root.iconbitmap(r"C:\Users\lijie\PycharmProjects\pythonProject\love.ico")
root.mainloop()
