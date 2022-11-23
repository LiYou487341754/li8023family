import sys
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from tkinter.messagebox import askyesno
from tkinter import messagebox
from tkinter import font


class VersionGui(object):
    def __init__(self, window_name):
        self.window_name = window_name
        self.window_name.title("文本存储查看器")
        self.window_name.resizable(True, True)
        self.window_name.attributes('-topmost', 0.5)
        self.w = self.window_name.winfo_screenwidth()
        self.h = self.window_name.winfo_screenheight()
        self.window_name.geometry("700x400+%d+%d" % ((self.w-700)/2, (self.h-400)/2))
        self.window_name.attributes('-topmost', 1)
        # self.window_name.protocol('WM_DELETE_WINDOW', self.close_window)
        # 组件容器创建
        self.window_name.panedwindow = PanedWindow(master=self.window_name, orient='vertical')
        self.window_name.panedwindow.pack()
        self.input_frame = ttk.Frame(master=self.window_name.panedwindow)  # 创建存放文本输入,文本选择的容器
        self.window_name.panedwindow.add(self.input_frame)
        self.input_frame.pack()
        self.choose_day_frame = ttk.Frame(self.window_name.panedwindow)
        self.window_name.panedwindow.add(self.choose_day_frame)
        self.choose_day_frame.pack()
        self.choose_day_frame1 = ttk.Frame(self.window_name.panedwindow)
        self.window_name.panedwindow.add(self.choose_day_frame1)
        self.choose_day_frame1.pack()
        self.start_frame = ttk.Frame(self.window_name.panedwindow)
        self.window_name.panedwindow.add(self.start_frame)
        self.start_frame.pack()
        self.log_frame = ttk.Frame(self.window_name.panedwindow)
        self.window_name.panedwindow.add(self.log_frame)
        self.log_frame.pack()
        # 创建文本输入，文本选择
        self.input_frame.lable = ttk.Label(self.input_frame, text="输入文本地址", font=("华文行楷", 15))
        self.input_frame.lable.grid(padx=20, pady=0, row=0, column=0, sticky=W)
        self.v = StringVar()
        self.file_input_entry = ttk.Entry(self.input_frame, textvariable=self.v, font=('华文行楷', 15), width=30)
        self.file_input_entry.grid(padx=0, pady=0, row=0, column=1)
        style1 = ttk.Style()
        style1.configure("TButton", font=("华文行楷", 15))
        self.file_input_button = ttk.Button(self.input_frame, text="选择文件", command=self.file_input_path)
        self.file_input_button.grid(padx=10, pady=0, row=0, column=2)
        # 添加读写方式
        self.choose_day_frame.lable = ttk.Label(self.choose_day_frame, text="选择框", font=("华文行楷", 13))
        self.choose_day_frame.lable.grid(padx=40, pady=10, row=0, column=1)
        table = ['r', 'w', 'a']
        self.choose_day_frame_v = StringVar()
        self.choose_day_frame_v.set(table[0])
        style = ttk.Style()
        style.configure("TRadiobutton", font=("华文行楷", 12))
        self.choose_day_frame.radiobutton = ttk.Radiobutton(self.choose_day_frame, text="读取",
                                                            variable=self.choose_day_frame_v, value='r')
        self.choose_day_frame.radiobutton.grid(padx=20, pady=10, row=0, column=2)
        self.choose_day_frame.radiobutton = ttk.Radiobutton(self.choose_day_frame, text="重写",
                                                            variable=self.choose_day_frame_v, value='w')
        self.choose_day_frame.radiobutton.grid(padx=20, pady=10, row=0, column=3)
        self.choose_day_frame.radiobutton = ttk.Radiobutton(self.choose_day_frame, text="追加",
                                                            variable=self.choose_day_frame_v, value='a')
        self.choose_day_frame.radiobutton.grid(padx=20, pady=10, row=0, column=4)
        self.choose_font1 = ttk.Label(self.choose_day_frame1, text='字体', font=("华文行楷", 12), foreground='black')
        # self.familyVar = ['华文行楷', '楷体', '宋体']
        self.familyVar = font.families()
        self.choose_font_family1 = ttk.Combobox(self.choose_day_frame1, values=self.familyVar, font=("华文行楷", 12))
        self.choose_font_family1.set("华文行楷")
        self.choose_font2 = ttk.Label(self.choose_day_frame1, text='粗细', font=("华文行楷", 12), foreground='black')
        self.familyState = ['normal', 'bold', 'underline', 'italic', 'overstrike']
        self.choose_font_family2 = ttk.Combobox(self.choose_day_frame1, values=self.familyState, font=("华文行楷", 12))
        self.choose_font_family2.set("normal")
        self.choose_font3 = ttk.Label(self.choose_day_frame1, text='字号', font=("华文行楷", 12), foreground='black')
        self.familySize = list(range(10, 51))
        self.choose_font_family3 = ttk.Combobox(self.choose_day_frame1, values=self.familySize, font=("华文行楷", 12))
        self.choose_font_family3.set("10")
        self.choose_font1.grid(row=1, column=0)
        self.choose_font_family1.grid(row=1, column=1)
        self.choose_font2.grid(row=1, column=2)
        self.choose_font_family2.grid(row=1, column=3)
        self.choose_font3.grid(row=1, column=4)
        self.choose_font_family3.grid(row=1, column=5)
        self.start_run1 = ttk.Button(self.start_frame, text="读取", command=self.version, state='normal')
        self.start_run1.grid(padx=20, pady=0, row=0, column=1)
        self.start_run2 = ttk.Button(self.start_frame, text="清空", command=self.clear)
        self.start_run2.grid(padx=20, pady=0, row=0, column=2)
        self.start_run3 = ttk.Button(self.start_frame, text="写入", command=self.write)
        self.start_run3.grid(padx=20, pady=0, row=0, column=3)
        self.start_run4 = ttk.Button(self.start_frame, text="退出", command=self.window_name.quit)
        self.start_run4.grid(padx=20, pady=0, row=0, column=4)
        self.run_log_v = StringVar()
        self.run_log_sbar1 = Scrollbar(self.log_frame, orient='horizontal', relief='sunken', width=10, cursor='heart')
        self.run_log_sbar2 = Scrollbar(self.log_frame, orient="vertical", relief="sunken", width=10, cursor='arrow')

        self.run_log = Text(self.log_frame, font=('华文楷体', 13, "bold"), width=5500, height=3000,
                            yscrollcommand=self.run_log_sbar2.set, bd=1, xscrollcommand=self.run_log_sbar1.set)
        self.run_log.focus_set()
        self.run_log_sbar1.pack(fill="x", expand=True, side='bottom')
        self.run_log_sbar2.pack(fill='y', expand=True, side='right')
        self.run_log.pack(fill='both', expand=True)
        self.run_log_sbar1.config(command=self.run_log.xview)
        self.run_log_sbar2.config(command=self.run_log.yview)
        self.choose_font_family1.bind("<<ComboboxSelected>>", self.font)
        self.choose_font_family2.bind("<<ComboboxSelected>>", self.font)
        self.choose_font_family3.bind("<<ComboboxSelected>>", self.font)

    def close_window(self):
        # 退出关闭窗口
        ans = askyesno(title="文本存储查看器", message="是否退出文本存储查看器")
        if ans:
            self.window_name.destroy()
            sys.exit()
        else:
            return None

    def file_input_path(self):
        path_ = askopenfilename()
        self.file_input_entry.delete(0, 'end')
        self.file_input_entry.insert('end', path_)

    def version(self):
        if self.choose_day_frame_v.get() == 'w' or self.choose_day_frame_v.get() == 'a':
            self.start_run1['state'] = "distabled"
        else:
            self.start_run1['state'] = 'normal'
            self.readversion()
        # print(self.start_run1['state'])
        if self.start_run1['state'] == 'normal':
            self.readversion()

    def readversion(self):
        self.clear()
        if self.v.get() == '':
            messagebox.showinfo(title="文本存储查看器", message="请输入地址")
        elif self.choose_day_frame_v.get() == 'r':
            with open(str(self.v.get()), str(self.choose_day_frame_v.get()))as f:
                a = f.readlines()
                for i in range(len(a)):
                    self.run_log.insert('end', a[i])
        else:
            self.write()

    def clear(self):
        self.run_log.delete('0.0', 'end')

    def write(self):
        a = self.run_log.get('0.0', 'end')
        if self.choose_day_frame_v.get() == 'w' or self.choose_day_frame_v.get() == 'a':
            with open(str(self.v.get()), str(self.choose_day_frame_v.get()))as f:
                f.write(a)
        else:
            messagebox.showinfo(title="文本存储查看器", message="错误")

    def font(self, event):
        self.run_log.config(
            font=(self.choose_font_family1.get(), int(self.choose_font_family3.get()), self.choose_font_family2.get())
        )


if __name__ == '__main__':
    root = Tk()
    text = VersionGui(root)
    root.mainloop()
