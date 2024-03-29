import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import *
import threading
import subprocess as sub
import os
import time
import ffmpy


def firstpage():
    global frame1
    global frame2
    global frame9
    global currentpage
    # sw = window.winfo_screenwidth()
    # sh = window.winfo_screenheight()
    # w = 700
    # h = 500
    # window.geometry("{0}x{1}+{2}+{3}".format(w, h, int((sw - w) / 2), int((sh - h) / 2)))
    if currentpage != frame1:
        currentpage.pack_forget()  # 取消显示当前界面，并不是销毁
        currentpage = frame1
        currentpage.pack()  # 显示界面1


def secondpage():
    global frame1, frame2, frame9, currentpage
    # sw = window.winfo_screenwidth()
    # sh = window.winfo_screenheight()
    # w = 1080
    # h = 720
    # window.geometry("{0}x{1}+{2}+{3}".format(w, h, int((sw - w) / 2), int((sh - h) / 2)))
    if currentpage != frame2:
        currentpage.pack_forget()  # 取消显示当前界面，并不是销毁
        currentpage = frame2
        currentpage.pack()  # 显示界面2


def threepage():
    global frame1, frame2, frame9, currentpage
    if currentpage != frame9:
        currentpage.pack_forget()
        currentpage = frame9
        currentpage.pack()


# 按钮对应的功能
def create_frame():
    # 界面一
    global frame1, frame2, frame9, currentpage
    frame1 = tk.Frame(window, relief='sunken')
    frame3 = tk.Frame(frame1, relief="sunken")
    frame4 = tk.Frame(frame1, relief="sunken")
    frame5 = tk.Frame(frame1, relief='sunken')
    frame3.pack()
    frame4.pack()
    frame5.pack()

    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.daemon = True
        t.start()

    def thread_it1(func, *args):
        t1 = threading.Thread(target=func, args=args)
        t1.daemon = True
        t1.start()

    def thread_it2(func, *args):
        t2 = threading.Thread(target=func, args=args)
        t2.daemon = True
        t2.start()

    def conversion():
        listbox1.delete('0', 'end')
        listbox1.insert('0', '开始转换')
        source_file = entry3.get()
        name = source_file.split('/')[-1].split('.')[0]
        sink_file = entry4.get() + '/' + name + "." + layout.get()
        listbox1.insert('end', '转换中........')
        try:
            ff = ffmpy.FFmpeg(
                inputs={source_file: None},
                outputs={sink_file: None})
            ff.run()
            window.update()
            listbox1.insert('end', "转换成功")
            window.update()
        except Exception as e:
            listbox1.insert('end', e)
            listbox1.insert('end', "转换失败")

    def select_way():
        waypath_ = askopenfilename()
        entry3.insert('0', waypath_)

    def selection_address():
        if len(entry4.get()) == 0:
            path_ = askdirectory()
            entry4.insert("0", path_)
        else:
            if not os.path.exists(entry4.get()):
                os.mkdir(entry4.get())

    def select_address():
        if len(entry2.get()) == 0:
            path_ = askdirectory()
            window.update()
            time.sleep(5)
            entry2.insert('end', path_)
            listbox.delete('0', 'end')
        else:
            if not os.path.exists(entry2.get()):
                os.mkdir(entry2.get())
                path_ = entry2.get()
                window.update()
                time.sleep(5)
                entry2.insert('end', path_)
                listbox.delete('0', 'end')
        try:
            listbox.delete("0", 'end')
            listbox.insert('0', '正在获取视频信息')
            cmd0 = f'you-get -i {entry1.get()}'
            window.update()
            p = sub.Popen(cmd0, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            for line in iter(p.stdout.readline, b''):
                listbox.insert('end', line.decode('UTF-8'))
                if not sub.Popen.poll(p) is None:
                    if line == "":
                        break
            p.stdout.close()
            window.update()
        except Exception as e:
            listbox.insert("end", "错误提示:")
            listbox.insert('end', e)
            listbox.insert("end", "获取信息失败")

    def select_address1():
        if len(entry6.get()) == 0:
            path_ = askdirectory()
            window.update()
            entry6.insert('end', path_)
            listbox2.delete('0', 'end')
            listbox2.insert('0', '开始获取视频信息')
        else:
            if not os.path.exists(entry6.get()):
                os.mkdir(entry6.get())
                path_ = entry6.get()
                window.update()
                entry6.insert('end', path_)
                listbox2.delete('0', 'end')
                listbox2.insert('0', '正在获取视频信息')
        try:
            window.update()
            window.update()
            cmd1 = f'you-get -i --playlist {entry5.get()}'
            window.update()
            p = sub.Popen(cmd1, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            for line in iter(p.stdout.readline, b''):
                listbox2.insert('end', line.decode('UTF-8'))
                if not sub.Popen.poll(p) is None:
                    if line == "":
                        break
            p.stdout.close()
            listbox2.insert('end', '获取结束')
            window.update()
            window.update()
        except Exception as e:
            listbox2.insert("end", "错误提示:")
            listbox2.insert('end', e)
            listbox2.insert("end", "获取信息失败")

    def download():
        window.update()
        listbox.delete('0', 'end')
        listbox.insert('0', "开始下载")
        try:
            window.update()
            urls = entry1.get()
            dirctory = entry2.get()
            difinition = select_download.get()
            difinit = '--format=' + difinition
            window.update()
            window.update()
            listbox.insert("end", "正在下载..........")
            cmd2 = f'you-get -o {dirctory} {difinit} {urls}'
            window.update()
            p = sub.Popen(cmd2, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            for line in iter(p.stdout.readline, b''):
                listbox.insert('end', line.decode('UTF-8'))
                if not sub.Popen.poll(p) is None:
                    if line == "":
                        break
            p.stdout.close()
            window.update()
            listbox.insert('end', "下载成功")
        except Exception as e:
            listbox.insert("end", "错误提醒:")
            listbox.insert('end', e)
            listbox.insert('end', '下载失败')

    def download1():
        window.update()
        listbox2.delete('0', 'end')
        listbox2.insert('0', "开始下载")
        window.update()
        urls = entry5.get()
        dirctory1 = entry6.get()
        difinition1 = select_download1.get()
        difinit1 = '--format=' + difinition1
        window.update()
        try:
            window.update()
            listbox2.insert("end", "正在下载..........")
            window.update()
            cmd3 = f'you-get -o {dirctory1} --playlist  {difinit1}  {urls}'
            window.update()
            p = sub.Popen(cmd3, stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
            for line in iter(p.stdout.readline, b''):
                listbox2.insert('end', line.decode('UTF-8'))
                if not sub.Popen.poll(p) is None:
                    if line == "":
                        break
            p.stdout.close()
            listbox2.insert('end', "下载成功")
        except Exception as e:
            listbox2.insert("end", "错误提醒:")
            listbox2.insert('end', e)
            listbox2.insert('end', '下载失败')

    def state():
        button1.config(state='normal')

    def clear0():
        entry1.delete(0, 'end')

    def clear1():
        entry2.delete(0, 'end')

    def clear2():
        entry5.delete(0, 'end')

    def clear3():
        entry6.delete(0, 'end')

    def clear4():
        entry3.delete(0, 'end')

    def clear5():
        entry4.delete(0, 'end')

    label1 = ttk.Label(frame3, text="\t下载网址:", font=("华文行楷", 13), foreground='black', anchor='e',
                       justify='right', takefocus=True)
    url = tk.StringVar()
    entry1 = ttk.Entry(frame3, textvariable=url, font=("华文新魏", 13, 'bold'), foreground='black',
                       takefocus=True,
                       width=36)
    button1 = ttk.Button(frame4, text="确认下载", state='disabled', command=lambda: thread_it(download))
    label2 = ttk.Label(frame3, text="     选择下载地址:", font=("华文行楷", 13), foreground="black",
                       anchor="e", justify='right')
    address = tk.StringVar()
    entry2 = ttk.Entry(frame3, textvariable=address, font=("华文新魏", 13, 'bold'), width=36)
    button2 = ttk.Button(frame3, text="选 择", command=lambda: thread_it(select_address))
    label3 = ttk.Label(frame3, text="         选择清晰度:", font=("华文行楷", 13), foreground='black',
                       anchor='e', justify='right')
    select_download = tk.StringVar()
    style = ttk.Style()
    style.configure("TRadiobutton", font=("华文新魏", 12, 'bold'))
    radiobutton1 = ttk.Radiobutton(frame4, text="dash-flv", value='dash-flv', variable=select_download,
                                   command=lambda: thread_it(state), takefocus=False)
    radiobutton2 = ttk.Radiobutton(frame4, text='dash-flv720', value='dash-flv720',
                                   variable=select_download, command=lambda: thread_it(state), takefocus=False)
    radiobutton3 = ttk.Radiobutton(frame4, text='dash-flv480', value='dash-flv480',
                                   variable=select_download, command=lambda: thread_it(state),
                                   takefocus=False)
    radiobutton4 = ttk.Radiobutton(frame4, text='dash-flv360', value='dash-flv360',
                                   variable=select_download, command=lambda: thread_it(state),
                                   takefocus=False)
    radiobutton5 = ttk.Radiobutton(frame4, text="flv", value='flv', variable=select_download,
                                   command=lambda: thread_it(state), takefocus=False)
    radiobutton6 = ttk.Radiobutton(frame4, text='flv720', value='flv720', variable=select_download,
                                   command=lambda: thread_it(state), takefocus=False)
    radiobutton7 = ttk.Radiobutton(frame4, text='flv480', value='flv480', variable=select_download,
                                   command=lambda: thread_it(state), takefocus=False)
    radiobutton8 = ttk.Radiobutton(frame4, text='flv360', value='flv360', variable=select_download,
                                   command=lambda: thread_it(state), takefocus=False)
    but1 = ttk.Button(frame4, text="网址清空", command=clear0)
    but2 = ttk.Button(frame4, text='地址清空', command=clear1)
    but3 = ttk.Button(frame4, text='退出程序', command=lambda: (window.quit))
    xscrollbar = tk.Scrollbar(frame5, orient='horizontal')
    yscrollbar = tk.Scrollbar(frame5, orient='vertical')
    listbox = tk.Listbox(frame5, font=("华文新魏", 13, 'bold'), xscrollcommand=xscrollbar.set,
                         yscrollcommand=yscrollbar.set, width=500, height=500)
    xscrollbar.config(command=listbox.xview)
    yscrollbar.config(command=listbox.yview)
    listbox.insert("0", '软件说明:')
    listbox.insert('end', '首先输入下载网址')
    listbox.insert('end', "选择视频保存路径或者输入一个路径")
    listbox.insert('end', '再查看视频的清晰度')
    listbox.insert('end', '选择清晰度')
    listbox.insert('end', '选择清晰度后下载视频')
    listbox.insert('end', '提醒(只有选择清晰度后下载按钮才开启正常状态)')

    label1.grid(row=0, column=0, padx=10, pady=5)
    entry1.grid(row=0, column=1, padx=10, pady=5)
    button1.grid(row=2, column=2, padx=10, pady=5)
    label2.grid(row=1, column=0, padx=10, pady=5)
    entry2.grid(row=1, column=1, padx=10, pady=5)
    button2.grid(row=1, column=2, padx=10, pady=5)
    label3.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    radiobutton1.grid(row=0, column=0, padx=25, pady=5, sticky="w")
    radiobutton2.grid(row=0, column=1, padx=25, pady=5, sticky="w")
    radiobutton3.grid(row=0, column=2, padx=25, pady=5, sticky="e")
    radiobutton4.grid(row=0, column=3, padx=25, pady=5, sticky="e")
    radiobutton5.grid(row=1, column=0, padx=25, pady=5, sticky="w")
    radiobutton6.grid(row=1, column=1, padx=25, pady=5, sticky="w")
    radiobutton7.grid(row=1, column=2, padx=65, pady=5, sticky="e")
    radiobutton8.grid(row=1, column=3, padx=65, pady=5, sticky="e")
    but1.grid(row=2, column=0, sticky='w')
    but2.grid(row=2, column=1)
    but3.grid(row=2, column=3)
    xscrollbar.pack(side='bottom', fill='x', expand=True)
    yscrollbar.pack(side='right', fill='y', expand=True)
    listbox.pack(fill='both', expand=True)

    currentpage = frame1
    currentpage.pack()
    # 界面二
    frame2 = tk.Frame(window)
    # frame2.pack_propagate(False)
    frame6 = tk.Frame(frame2, relief='sunken')
    frame7 = tk.Frame(frame2, relief='sunken')
    frame8 = tk.Frame(frame2, relief='sunken')
    frame14 = tk.Frame(frame2, relief='sunken')
    #  容器分布
    frame6.pack()
    frame7.pack()
    frame14.pack()
    frame8.pack()
    # 控件
    label4 = ttk.Label(frame6, text="视频路径:", font=("华文行楷", 13))
    way = tk.StringVar()
    entry3 = ttk.Entry(frame6, textvariable=way, font=("华文新魏", 12, 'bold'), width=36, exportselection=True)
    style0 = ttk.Style()
    style0.configure("TButton", font=("华文行楷", 13))
    button3 = ttk.Button(frame6, text='选 择', command=lambda: thread_it2(select_way))
    label5 = ttk.Label(frame6, text="转换格式:", font=("华文行楷", 13))
    layout = tk.StringVar()
    style1 = ttk.Style()
    style1.configure("TRadiobutton", font=("华文新魏", 12, 'bold'))
    radiobutton9 = ttk.Radiobutton(frame6, text="mp4", value="mp4", variable=layout, takefocus=False)
    radiobutton10 = ttk.Radiobutton(frame6, text="flv", value="flv", variable=layout, takefocus=False)
    radiobutton11 = ttk.Radiobutton(frame6, text="avi", value="avi", variable=layout, takefocus=False)
    radiobutton12 = ttk.Radiobutton(frame6, text="mov", value="mov", variable=layout, takefocus=False)
    label6 = ttk.Label(frame7, text="保存地址:", font=("华文行楷", 13))
    saveway = tk.StringVar()
    entry4 = ttk.Entry(frame7, textvariable=saveway, font=("华文新魏", 12, 'bold'), width=36, exportselection=True)
    button4 = ttk.Button(frame7, text="选择路径", command=lambda: thread_it2(selection_address))
    button5 = ttk.Button(frame14, text='路径清空', command=lambda: thread_it2(clear4))
    button6 = ttk.Button(frame14, text='地址清空', command=lambda: thread_it2(clear5))
    button7 = ttk.Button(frame14, text="开始转换", command=lambda: thread_it2(conversion))
    button8 = ttk.Button(frame14, text='退出程序', command=lambda: thread_it2(window.quit))
    xscrollbar1 = ttk.Scrollbar(frame8, orient='horizontal')
    yscrollbar1 = ttk.Scrollbar(frame8, orient='vertical')
    listbox1 = tk.Listbox(frame8, relief="sunken", font=("华文新魏", 12, 'bold'), takefocus=True,
                          xscrollcommand=xscrollbar1.set, yscrollcommand=yscrollbar1.set, width=500, height=500)
    xscrollbar1.configure(command=listbox1.xview)
    yscrollbar1.configure(command=listbox1.yview)
    # 控件分布
    label4.grid(row=0, column=0, padx=10, pady=5)
    entry3.grid(row=0, column=1, padx=10, pady=5)
    button3.grid(row=0, column=2, padx=10, pady=5)
    label5.grid(row=1, column=0, padx=10, pady=5)
    radiobutton9.grid(row=2, column=0, padx=25, pady=5, sticky="w")
    radiobutton10.grid(row=2, column=1, padx=25, pady=5, sticky="e")
    radiobutton11.grid(row=3, column=0, padx=25, pady=5, sticky="w")
    radiobutton12.grid(row=3, column=1, padx=10, pady=5, sticky="e")
    label6.grid(row=0, column=0, padx=10, pady=5)
    entry4.grid(row=0, column=1, padx=10, pady=5)
    button4.grid(row=0, column=2, padx=10, pady=5)
    button5.grid(row=0, column=0, padx=10, sticky='w')
    button6.grid(row=0, column=1, padx=10, sticky='w')
    button7.grid(row=0, column=2, padx=10)
    button8.grid(row=0, column=3, padx=10)
    xscrollbar1.pack(side='bottom', fill='x', expand=True)
    yscrollbar1.pack(side='right', fill='y', expand=True)
    listbox1.pack(fill='both', expand=True)

    # 界面三
    frame9 = tk.Frame(window)
    frame10 = tk.Frame(frame9, relief='sunken')
    frame11 = tk.Frame(frame9, relief='sunken')
    frame12 = tk.Frame(frame9, relief='sunken')
    frame13 = tk.Frame(frame9, relief='sunken')
    # 容器分布
    frame10.pack()
    frame11.pack()
    frame12.pack()
    frame13.pack()
    # 控件
    address1 = tk.StringVar()
    label7 = ttk.Label(frame10, text='下载网址:', font=("华文行楷", 13), foreground='black', anchor='e')
    entry5 = ttk.Entry(frame10, textvariable=address1, font=("华文新魏", 13, 'bold'), foreground='black', justify='left',
                       exportselection=True, takefocus=True, width=36)
    label8 = ttk.Label(frame10, text="保存地址:", font=("华文行楷", 13), foreground='black', anchor='e')
    button7 = ttk.Button(frame10, text="选 择", command=lambda: thread_it1(select_address1))
    address2 = tk.StringVar()
    entry6 = ttk.Entry(frame10, textvariable=address2, font=("华文新魏", 13, 'bold'), foreground='black', justify='left',
                       exportselection=True, takefocus=True, width=36)
    label9 = ttk.Label(frame10, text="         选择清晰度:", font=("华文行楷", 13), foreground='black',
                       anchor='e', justify='right')
    select_download1 = tk.StringVar()
    style = ttk.Style()
    style.configure("TRadiobutton", font=("华文新魏", 12, 'bold'))
    radiobutton13 = ttk.Radiobutton(frame11, text="dash-flv", value='dash-flv', variable=select_download1,
                                    takefocus=False)
    radiobutton14 = ttk.Radiobutton(frame11, text='dash-flv720', value='dash-flv720',
                                    variable=select_download1, takefocus=False)
    radiobutton15 = ttk.Radiobutton(frame11, text='dash-flv480', value='dash-flv480',
                                    variable=select_download1,
                                    takefocus=False)
    radiobutton16 = ttk.Radiobutton(frame11, text='dash-flv360', value='dash-flv360',
                                    variable=select_download1,
                                    takefocus=False)
    radiobutton17 = ttk.Radiobutton(frame11, text="flv", value='flv', variable=select_download1,
                                    takefocus=False)
    radiobutton18 = ttk.Radiobutton(frame11, text='flv720', value='flv720', variable=select_download1,
                                    takefocus=False)
    radiobutton19 = ttk.Radiobutton(frame11, text='flv480', value='flv480', variable=select_download1,
                                    takefocus=False)
    radiobutton20 = ttk.Radiobutton(frame11, text='flv360', value='flv360', variable=select_download1,
                                    takefocus=False)

    button8 = ttk.Button(frame12, text='网址清空', command=lambda: thread_it1(clear2))
    button9 = ttk.Button(frame12, text='地址清空', command=lambda: thread_it1(clear3))
    button10 = ttk.Button(frame12, text="确认下载", command=lambda: thread_it1(download1))
    button11 = ttk.Button(frame12, text="退出程序", command=lambda: thread_it1(window.quit))
    xscrollbar = tk.Scrollbar(frame13, orient='horizontal')
    yscrollbar = tk.Scrollbar(frame13, orient='vertical')
    listbox2 = tk.Listbox(frame13, font=("华文新魏", 13, 'bold'), xscrollcommand=xscrollbar.set,
                          yscrollcommand=yscrollbar.set, width=500, height=500)
    xscrollbar.config(command=listbox2.xview)
    yscrollbar.config(command=listbox2.yview)
    # 控件分布
    label7.grid(row=0, column=0, padx=10, pady=5)
    entry5.grid(row=0, column=1, padx=10, pady=5)
    label8.grid(row=1, column=0, padx=10, pady=5)
    entry6.grid(row=1, column=1, padx=10, pady=5)
    button7.grid(row=1, column=2, padx=10, pady=5)
    label9.grid(row=2, column=0, sticky='w', padx=10, pady=5)
    radiobutton13.grid(row=0, column=0, padx=25, pady=5, sticky="w")
    radiobutton14.grid(row=0, column=1, padx=25, pady=5, sticky="w")
    radiobutton15.grid(row=0, column=2, padx=25, pady=5, sticky="e")
    radiobutton16.grid(row=0, column=3, padx=25, pady=5, sticky="e")
    radiobutton17.grid(row=1, column=0, padx=25, pady=5, sticky="w")
    radiobutton18.grid(row=1, column=1, padx=25, pady=5, sticky="w")
    radiobutton19.grid(row=1, column=2, padx=65, pady=5, sticky="e")
    radiobutton20.grid(row=1, column=3, padx=65, pady=5, sticky="e")
    button8.grid(row=0, column=0, padx=40)
    button9.grid(row=0, column=1, padx=40)
    button10.grid(row=0, column=2, padx=40)
    button11.grid(row=0, column=3, padx=40)
    xscrollbar.pack(side='bottom', fill='x', expand=True)
    yscrollbar.pack(side='right', fill='y', expand=True)
    listbox2.pack(fill='both', expand=True)


# 创建窗口
window = tk.Tk()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()
w = 700
h = 500
window.geometry("{0}x{1}+{2}+{3}".format(w, h, int((sw - w) / 2), int((sh - h) / 2)))
window.title("哔哩视频下载器")
window.resizable(True, True)
window.update()


# 按钮框架
frame0 = tk.Frame(window, height=30, width=500)
frame0.pack(side='top', fill='both', expand=1)

# 界面切换按钮
btn = tk.StringVar()
btn1 = ttk.Button(frame0, text='视频下载', command=firstpage)
btn1.pack(side="left")

btn2 = ttk.Button(frame0, text='批量下载', command=threepage)
btn2.pack(side='left', expand=True)

btn3 = ttk.Button(frame0, text='格式转换', command=secondpage)
btn3.pack(side='right')

# 首先打开主界面
if __name__ == "__main__":
    global frame1, frame2, frame9, currentpage
    create_frame()
    window.mainloop()
