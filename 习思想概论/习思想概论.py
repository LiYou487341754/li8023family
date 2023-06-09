import random
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import Image, ImageTk
from tkinter import messagebox


class AnswerQuestion(object):
    def __init__(self, window_name):
        self.window = None
        self.window_name = window_name
        self.window_name.title('答题小游戏')
        self.width = 450
        self.height = 310
        self.screenwidth = self.window_name.winfo_screenwidth()
        self.screenheight = self.window_name.winfo_screenheight()
        self.window_name.geometry("{0}x{1}+{2}+{3}".format(self.width, self.height, int(self.screenwidth-self.width)//2,
                                                           int(self.screenheight-self.height)//2))
        self.window_name.resizable(False, False)
        # 组件容器创建
        self.panedwindow = PanedWindow(master=self.window_name, orient='vertical')
        self.panedwindow1 = None
        self.panedwindow2 = None
        self.panedwindow3 = None
        self.panedwindow4 = None
        self.choose_box = None
        self.submission_frame = None
        self.panedwindow.grid(row=0, column=0)
        self.more_than_one = StringVar()
        self.option = StringVar()
        self.question_a = StringVar()
        self.question_b = StringVar()
        self.question_c = StringVar()
        self.question_d = StringVar()
        self.mode_choose = StringVar()
        self.questions = StringVar()
        self.box = {}
        self.banks = ['sign.db', 'sign1.db', 'sign2.db', 'sign3.db']
        self.item_bank = './' + self.banks[0]
        self.bank = StringVar()
        self.bank_question = None
        self.number = [i * 0 for i in range(len(self.question_bank()))]
        self.familyVar = font.families()
        self.familySize = list(range(10, 29))
        self.familyColor = None
        self.familyState = ['normal', 'bold', 'underline', 'italic', 'overstrike']
        self.choose_font_family1 = None
        self.choose_font_family2 = None
        self.choose_font_family3 = None
        self.display_anwser_label = None
        self.number_question_number = []
        self.question_select_a = None
        self.question_select_b = None
        self.question_select_c = None
        self.question_select_d = None
        self.username_entry1 = None
        self.username_entry2 = None
        self.username_entry3 = None
        self.username_entry4 = None
        self.username_entry5 = None
        self.password_entry1 = None
        self.password_entry2 = None
        self.password_entry3 = None
        self.password_entry4 = None
        self.password_entry5 = None
        self.password_entry6 = None
        self.password_entry7 = None
        self.password_entry8 = None
        self.result_frame = None
        self.choose_frame = None
        self.function_frame = None
        self.result = None
        self.result1 = None
        self.result2 = None
        self.result3 = None
        self.result4 = None
        self.question = None
        self.label = None
        self.score = None
        self.answer = []
        self.compute = 1
        self.count = 0
        self.scores = 0
        self.serial_number = [i for i in range(1, len(self.question_bank()) + 1)]
        self.title_frame = ttk.Frame(master=self.panedwindow, width=self.width, height=90)
        self.panedwindow.add(self.title_frame)
        self.sign_frame = ttk.Frame(self.panedwindow)
        self.panedwindow.add(self.sign_frame)
        self.choose_day_frame = ttk.Frame(self.panedwindow)
        self.panedwindow.add(self.choose_day_frame)
        self.set_frame = ttk.Frame(self.panedwindow)
        self.panedwindow.add(self.set_frame)
        self.title_frame.pack()
        self.sign_frame.pack()
        self.choose_day_frame.pack()
        self.set_frame.pack()
        # 登录组件创建
        photo = Image.open(r".\风景5.jpg")
        self.photo = ImageTk.PhotoImage(photo.resize((self.width, 90)))
        self.title = Label(self.title_frame, width=self.width, height=90, image=self.photo)
        self.title.grid(pady=1)
        self.username = ttk.Label(self.sign_frame, text='账号:', font=("华文新魏", 13))
        self.username_v = StringVar()
        self.username_validate = root.register(self.username_validate)
        self.username_entry = ttk.Entry(self.sign_frame, textvariable=self.username_v, font=("华文新魏", 13), width=21,
                                        validate='key', validatecommand=(self.username_validate, '%P'))
        self.password = ttk.Label(self.sign_frame, text='密码:', font=("华文新魏", 13))
        self.password_v = StringVar()
        self.password_validate = root.register(self.password_validate)
        self.password_entry = ttk.Entry(self.sign_frame, textvariable=self.password_v, font=("华文新魏", 13), show='.',
                                        width=21, validate='key', validatecommand=(self.password_validate, '%P'))
        self.checkbutton = ttk.Checkbutton(self.password_entry, text='')
        self.multiple_choies1 = StringVar()
        self.multiple_choies2 = StringVar()
        style = ttk.Style()
        style.configure('TCheckbutton')
        self.choies1 = ttk.Checkbutton(self.choose_day_frame, text='自动登录', onvalue=1, offvalue=0,
                                       variable=self.multiple_choies1, takefocus=False)
        self.choies2 = ttk.Checkbutton(self.choose_day_frame, text='记住密码', onvalue=1, offvalue=0,
                                       variable=self.multiple_choies2, takefocus=False)
        self.button1 = ttk.Button(self.choose_day_frame, text='找回密码', command=self.find_password)
        self.sign = ttk.Button(self.choose_day_frame, text=' 登 录 ', command=self.sign_up)
        self.button2 = ttk.Button(self.set_frame, text='注册账号', command=self.registered_account)
        self.button3 = ttk.Button(self.set_frame, text='修改密码', command=self.change)
        self.button4 = ttk.Button(self.set_frame, text='注销账号', command=self.cancel_account)
        self.username.grid(row=0, column=1, padx=(20, 10), pady=0)
        self.username_entry.grid(row=0, column=2, padx=14, pady=10)
        self.password.grid(row=1, column=1, padx=(20, 10),  pady=10)
        self.password_entry.grid(row=1, column=2, padx=14, pady=10)
        self.choies1.grid(row=0, column=0, padx=(25, 17), pady=5)
        self.choies2.grid(row=0, column=1, padx=10, pady=5)
        self.button1.grid(row=0, column=2, padx=17, pady=5)
        self.sign.grid(row=1, column=0, padx=(8, 0), columnspan=3, ipadx=98)
        self.button2.grid(row=2, column=0, padx=(15, 5), pady=5)
        self.button3.grid(row=2, column=1, padx=6, pady=5)
        self.button4.grid(row=2, column=2, padx=5, pady=5)
        # 菜单
        self.menu = Menu(self.window_name, tearoff=False)
        self.menu.add_command(label='剪切(T)', font=('华文新魏', 12), command=self.callback_one)
        self.menu.add_command(label='复制(C)', font=('华文新魏', 12), command=self.callback_two)
        self.menu.add_command(label='粘贴(P)', font=('华文新魏', 12), command=self.callback_three)
        self.menu.add_command(label='刷新(E)', font=('华文新魏', 12), command=self.callback_four)
        self.window_name.bind("<Button-3>", self.pop)
        self.window_name.bind("<Return>", self.sign_down)
        self.username_entry.bind('<KeyPress-T>', self.callback_frist)
        self.username_entry.bind('<KeyPress-C>', self.callback_second)
        self.username_entry.bind('<KeyPress-P>', self.callback_third)
        self.username_entry.bind('<KeyPress-E>', self.callback_fourth)

    def creat_window(self):
        self.window_name.withdraw()
        self.window = Toplevel(self.window_name)
        self.window.geometry('{0}x{1}+{2}+{3}'.format(1000, 600, int(self.screenwidth - 1000) // 2,
                                                      int(self.screenheight - 700) // 2))
        self.window.protocol('WM_DELETE_WINDOW', self.on_closing)
        left_panedwindow = PanedWindow(self.window, sashrelief='sunken', opaqueresize=False)
        left_panedwindow.pack(fill='both', expand=True)
        right_panedwindow = PanedWindow(self.window, sashrelief='sunken', orient='horizontal',
                                        opaqueresize=False)
        left_panedwindow.add(right_panedwindow)
        self.function_frame = Frame(right_panedwindow)
        right_panedwindow.add(self.function_frame, minsize=220)
        answer_frame = Frame(self.function_frame)
        control_panel = Frame(self.function_frame)
        self.choose_box = Frame(self.function_frame)
        self.submission_frame = Frame(self.function_frame)
        self.result_frame = Frame(self.function_frame)
        answer_frame.pack()
        control_panel.pack()
        self.choose_box.pack()
        self.submission_frame.pack()
        self.result_frame.pack()
        question_bank = Frame(right_panedwindow)
        right_panedwindow.add(question_bank)
        font_size_frame = Frame(question_bank)
        question_frame = Frame(question_bank)
        self.choose_frame = Frame(question_bank)
        sure_frame = Frame(question_bank)
        display_anwser = Frame(question_bank)
        font_size_frame.pack(anchor='sw', padx=(10, 0))
        question_frame.pack(anchor='sw', padx=(10, 0))
        self.choose_frame.pack(anchor='sw', padx=(10, 0))
        sure_frame.pack(anchor='sw', padx=(10, 0))
        display_anwser.pack(anchor='sw', padx=(10, 0))
        control = Label(answer_frame, text='设置', font=('华文新魏', 20))
        control.pack(side='top', pady=20)
        mode = Label(control_panel, text='模式', font=('华文新魏', 15))
        mode.grid(row=0, column=0, pady=10)
        style = ttk.Style()
        style.configure('TRadiobutton', font=('华文新魏', 15))
        question_choose_one = ttk.Radiobutton(control_panel, text='答题', takefocus=False,
                                              variable=self.mode_choose, value='A', command=self.mode_question)
        question_choose_one.grid(row=1, column=1)
        question_choose_two = ttk.Radiobutton(control_panel, text='游戏', takefocus=False,
                                              variable=self.mode_choose, value='B', command=self.mode_question1)
        question_choose_two.grid(row=1, column=2)
        questions = ttk.Label(control_panel, text="题型", font=('华文新魏', 15))
        questions.grid(row=4, column=0)
        more_lable = ttk.Radiobutton(control_panel, text='单选', takefocus=False, variable=self.more_than_one,
                                     value='O', command=self.display_box)
        more_lable.grid(row=5, column=1, pady=10)
        one_lable = ttk.Radiobutton(control_panel, text='多选', takefocus=False, variable=self.more_than_one,
                                    value='M', command=self.display_box)
        one_lable.grid(row=5, column=2, pady=10)

        question_label = ttk.Label(control_panel, text="题库", font=('华文新魏', 15))
        question_label.grid(row=6, column=0)
        self.bank_question = ttk.Combobox(control_panel, values=self.banks, justify='center')
        self.bank_question.grid(row=6, column=1, columnspan=2, pady=(10, 10))
        self.bank_question.set(self.banks[0])
        self.mode_choose.set('A')
        self.more_than_one.set('O')
        self.display_box()
        button_style = ttk.Style()
        button_style.configure('my.TButton', font=('华文新魏', 12))
        submission = ttk.Button(self.submission_frame, text='提交', command=self.get_score, style='my.TButton')
        submission.grid(row=0, column=0)
        self.score = ttk.Label(self.submission_frame, text='得分:', font=('华文新魏', 15))
        self.score.grid(row=1, column=1)
        quit_sign = ttk.Button(self.result_frame, text='答题重置', command=self.reset, style='my.TButton')
        quit_sign.pack(ipadx=20, pady=5, padx=(10, 0))
        services_change = ttk.Button(self.result_frame, text='退出登录', command=self.quit, style='my.TButton')
        services_change.pack(ipadx=20, pady=5, padx=(10, 0))
        bigfont = font.Font(family="华文新魏", size=12)
        self.window.option_add("*TCombobox*Listbox*Font", bigfont)
        choose_font1 = ttk.Label(font_size_frame, text='字体:', font=("华文行楷", 12), foreground='black')
        self.choose_font_family1 = ttk.Combobox(font_size_frame, values=self.familyVar, font=("华文新魏", 12))
        self.choose_font_family1.set("华文新魏")
        choose_font1.grid(row=0, column=0, padx=(0, 1), pady=5)
        self.choose_font_family1.grid(row=0, column=1)
        choose_font2 = ttk.Label(font_size_frame, text='粗细:', font=("华文行楷", 12), foreground='black')
        self.choose_font_family2 = ttk.Combobox(font_size_frame, values=self.familyState, font=("华文新魏", 12))
        self.choose_font_family2.set("normal")
        choose_font2.grid(row=0, column=2, padx=(1, 1))
        self.choose_font_family2.grid(row=0, column=3)
        choose_font3 = ttk.Label(font_size_frame, text='字号:', font=("华文行楷", 12), foreground='black')
        self.choose_font_family3 = ttk.Combobox(font_size_frame, values=self.familySize, font=("华文新魏", 12))
        self.choose_font_family3.set("18")
        choose_font3.grid(row=0, column=4, padx=(1, 1))
        self.choose_font_family3.grid(row=0, column=5)
        self.questions.set(self.question_bank()[self.count][0])
        self.question = Label(question_frame, textvariable=self.questions, font=('华文新魏', 19), wraplength=700,
                              justify='left', height=3)
        self.question.pack(anchor='sw', padx=(10, 0))
        previous_page = ttk.Button(sure_frame, text=' 上一页 ', command=self.previous_page, style='my.TButton')
        question_sure = ttk.Button(sure_frame, text=' 确 认 ', command=self.question_answer, style='my.TButton')
        next_page = ttk.Button(sure_frame, text=' 下一页 ', command=self.next_page, style='my.TButton')
        self.display_anwser_label = ttk.Label(display_anwser, text='答案为:', font=("华文新魏", 21), foreground='black')
        self.display_anwser_label.pack()
        previous_page.grid(row=0, column=0, pady=10, padx=(0, 20))
        question_sure.grid(row=0, column=1, padx=20)
        next_page.grid(row=0, column=2, padx=20)
        self.choose_font_family1.bind("<<ComboboxSelected>>", self.font)
        self.choose_font_family2.bind("<<ComboboxSelected>>", self.font)
        self.choose_font_family3.bind("<<ComboboxSelected>>", self.font)
        self.bank_question.bind("<<ComboboxSelected>>", self.change_bank)
        self.window.mainloop()

    def sign_data(self):
        conn = sqlite3.connect(self.item_bank)
        cur = conn.cursor()
        cur.execute("select * from sign")
        data = cur.fetchall()
        return data

    @staticmethod
    def code_data():
        conn = sqlite3.connect('./code.db')
        cur = conn.cursor()
        cur.execute("select * from code")
        data = cur.fetchall()
        return data

    def question_bank(self):
        con = sqlite3.connect(self.item_bank)
        cur = con.cursor()
        cur.execute('select * from question_bank')
        data = cur.fetchall()
        return data

    def question_bank1(self):
        con = sqlite3.connect(self.item_bank)
        cur = con.cursor()
        cur.execute('select * from question_bank2')
        data = cur.fetchall()
        return data

    def memory_data(self):
        con = sqlite3.connect(self.item_bank)
        cur = con.cursor()
        cur.execute('select * from memorys')
        data = cur.fetchall()
        return data

    @staticmethod
    def username_validate(content):
        if content.isdigit() or content == "":
            if len(content) <= 7:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def password_validate(content):
        if len(content) <= 16:
            return True
        else:
            return False

    def display_box(self):
        if self.more_than_one.get() == "O":
            self.serial_number = [i for i in range(1, len(self.question_bank()) + 1)]
            self.number = [i * 0 for i in range(len(self.question_bank()))]
        else:
            self.serial_number = [i for i in range(1, len(self.question_bank1()) + 1)]
            self.number = [i * 0 for i in range(len(self.question_bank1()))]
        self.count = 0
        self.choose_box.destroy()
        self.choose_box = Frame(self.function_frame)
        self.submission_frame.pack_forget()
        self.result_frame.pack_forget()
        self.box.clear()
        self.compute = 1
        for_get = self.choose_frame.slaves()
        for i in for_get:
            i.pack_forget()
        if self.more_than_one.get() == 'O':
            data = self.question_bank()
            long = len(self.question_bank()) / 4
            style = ttk.Style()
            style.configure('my.TRadiobutton', font=('华文新魏', 18), height=100)
            self.questions.set(self.question_bank()[self.count][0])
            self.question_select_a = ttk.Radiobutton(self.choose_frame, text=self.question_bank()[self.count][1],
                                                     variable=self.option, takefocus=False, style='my.TRadiobutton',
                                                     value='A')
            self.question_select_a.pack(anchor='sw', pady=5, padx=(10, 0))
            self.question_select_b = ttk.Radiobutton(self.choose_frame, text=self.question_bank()[self.count][2],
                                                     variable=self.option, value='B',
                                                     takefocus=False, style='my.TRadiobutton')
            self.question_select_b.pack(anchor='sw', pady=5, padx=(10, 0))
            self.question_select_c = ttk.Radiobutton(self.choose_frame, text=self.question_bank()[self.count][3],
                                                     variable=self.option, value='C',
                                                     takefocus=False, style='my.TRadiobutton')
            self.question_select_c.pack(anchor='sw', pady=5, padx=(10, 0))
            self.question_select_d = ttk.Radiobutton(self.choose_frame, text=self.question_bank()[self.count][4],
                                                     variable=self.option, value='D',
                                                     takefocus=False, style='my.TRadiobutton')
            self.question_select_d.pack(anchor='sw', pady=5, padx=(10, 0))
        else:
            data = self.question_bank1()
            long = len(self.question_bank1()) / 4
            style = ttk.Style()
            style.configure('my.TCheckbutton', font=('华文新魏', 18), height=100, wraplength=1000)
            self.questions.set(self.question_bank1()[self.count][0])
            self.question_select_a = ttk.Checkbutton(self.choose_frame, text=self.question_bank1()[self.count][1],
                                                     variable=self.question_a, takefocus=False, offvalue=0,
                                                     onvalue=1, style='my.TCheckbutton')
            self.question_select_a.pack(anchor='sw', pady=5, padx=(10, 0))
            self.question_select_b = ttk.Checkbutton(self.choose_frame, text=self.question_bank1()[self.count][2],
                                                     variable=self.question_b,
                                                     takefocus=False, offvalue=0, onvalue=1, style='my.TCheckbutton')
            self.question_select_b.pack(anchor='sw', pady=5, padx=(10, 0))
            self.question_select_c = ttk.Checkbutton(self.choose_frame, text=self.question_bank1()[self.count][3],
                                                     variable=self.question_c,
                                                     takefocus=False, offvalue=0, onvalue=1, style='my.TCheckbutton')
            self.question_select_c.pack(anchor='sw', pady=5, padx=(10, 0))
            self.question_select_d = ttk.Checkbutton(self.choose_frame, text=self.question_bank1()[self.count][4],
                                                     variable=self.question_d,
                                                     takefocus=False, offvalue=0, onvalue=1, style='my.TCheckbutton')
            self.question_select_d.pack(anchor='sw', pady=5, padx=(10, 0))
        if long.is_integer():
            for i in range(int(long)):
                for j in range(4):
                    if j == 0:
                        self.box[self.compute] = IntVar()
                        ttk.Checkbutton(self.choose_box, text='', takefocus=False, variable=self.box[self.compute],
                                        onvalue=self.compute, offvalue=0, command=self.jump_question) \
                            .grid(row=i, column=j, padx=(45, 6))
                        self.compute += 1
                    if j != 0:
                        self.box[self.compute] = IntVar()
                        ttk.Checkbutton(self.choose_box, text='', takefocus=False, variable=self.box[self.compute],
                                        onvalue=self.compute, offvalue=0, command=self.jump_question) \
                            .grid(row=i, column=j, padx=6)
                        self.compute += 1
        else:
            for i in range(int(long) + 1):
                for j in range(4):
                    if j == 0:
                        if self.compute != len(data) and self.compute < len(data):
                            self.box[self.compute] = IntVar()
                            ttk.Checkbutton(self.choose_box, text='', takefocus=False,
                                            variable=self.box[self.compute],
                                            onvalue=self.compute, offvalue=0, command=self.jump_question) \
                                .grid(row=i, column=j, padx=(45, 6))
                            self.compute += 1
                        elif self.compute == len(data):
                            self.box[self.compute] = IntVar()
                            ttk.Checkbutton(self.choose_box, text='', takefocus=False,
                                            variable=self.box[self.compute],
                                            onvalue=self.compute, offvalue=0, command=self.jump_question) \
                                .grid(row=i, column=j, padx=(45, 6))
                            self.compute += 1
                            break
                        else:
                            break
                    if j != 0:
                        if self.compute != len(data):
                            self.box[self.compute] = IntVar()
                            ttk.Checkbutton(self.choose_box, text='', takefocus=False,
                                            variable=self.box[self.compute],
                                            onvalue=self.compute, offvalue=0, command=self.jump_question) \
                                .grid(row=i, column=j, padx=6)
                            self.compute += 1
                        elif self.compute == len(data):
                            self.box[self.compute] = IntVar()
                            ttk.Checkbutton(self.choose_box, text='', takefocus=False,
                                            variable=self.box[self.compute],
                                            onvalue=self.compute, offvalue=0, command=self.jump_question) \
                                .grid(row=i, column=j, padx=6)
                            self.compute += 1
                            break
                        else:
                            break
        self.choose_box.pack()
        self.submission_frame.pack()
        self.result_frame.pack()

    def mode_question(self):
        self.serial_number = [i for i in range(1, len(self.question_bank()) + 1)]
        self.number = [i * 0 for i in range(len(self.question_bank()))]
        self.mode_choose.get()
        self.score.configure(text='得分:')
        if self.more_than_one.get() == 'O':
            for i in range(len(self.question_bank())):
                self.number[i] = 0
                self.box[i+1].set(0)
        else:
            for i in range(len(self.question_bank())):
                self.number[i] = 0
                self.box[i+1].set(0)
        self.count = 0
        self.compute = 1
        self.questions.set(self.question_bank()[self.count][0])
        self.question_select_a.configure(text=self.question_bank()[self.count][1])
        self.question_select_b.configure(text=self.question_bank()[self.count][2])
        self.question_select_c.configure(text=self.question_bank()[self.count][3])
        self.question_select_d.configure(text=self.question_bank()[self.count][4])
        self.question_a.set('')
        self.question_b.set('')
        self.question_c.set('')
        self.question_d.set('')

    def mode_question1(self):
        self.reset()
        self.serial_number = [i for i in range(1, len(self.question_bank1()) + 1)]
        self.number = [i * 0 for i in range(len(self.question_bank1()))]
        self.mode_choose.get()
        self.serial_number = [i for i in range(1, len(self.question_bank1()) + 1)]
        self.score.configure(text='得分:')
        if self.more_than_one.get() == 'O':
            for i in range(len(self.question_bank1())):
                self.number[i] = 0
                self.box[i+1].set(0)
        else:
            for i in range(len(self.question_bank1())):
                self.number[i] = 0
                self.box[i+1].set(0)
        self.count = 0
        self.compute = 1
        self.questions.set(self.question_bank1()[self.count][0])
        self.question_select_a.configure(text=self.question_bank1()[self.count][1])
        self.question_select_b.configure(text=self.question_bank1()[self.count][2])
        self.question_select_c.configure(text=self.question_bank1()[self.count][3])
        self.question_select_d.configure(text=self.question_bank1()[self.count][4])
        self.question_a.set('')
        self.question_b.set('')
        self.question_c.set('')
        self.question_d.set('')

    def update_memory(self):
        con = sqlite3.connect(self.item_bank)
        cur = con.cursor()
        cur.execute('delete from memorys where id=?', (1, ))
        cur.execute('insert into memorys(id, digit_one, digit_two, username, password) values(?, ?, ?, ?, ?)',
                    ('1', self.multiple_choies1.get(), self.multiple_choies2.get(),
                     self.username_entry.get(), self.password_entry.get()))
        con.commit()

    def menory_function(self):
        if len(self.memory_data()) != 0:
            for i in range(len(self.sign_data())):
                if self.memory_data()[0][3] == self.sign_data()[i][0]:
                    self.username_v.set(self.memory_data()[0][3])
                    if self.memory_data()[0][1] == '1' and self.memory_data()[0][2] == '1':
                        self.password_v.set(self.memory_data()[0][4])
                        self.multiple_choies1.set('1')
                        self.multiple_choies2.set('1')
                        self.update_memory()
                        self.sign_up()
                    elif self.memory_data()[0][2] == '1':
                        self.multiple_choies2.set('1')
                        self.password_v.set(self.memory_data()[0][4])

    def previous_page(self):
        self.display_anwser_label.configure(text="答案为:")
        if self.more_than_one.get() == 'M':
            if self.mode_choose.get() == 'A':
                data = self.question_bank1()
                if self.count != 0:
                    self.count -= 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])
                    self.question_a.set('')
                    self.question_b.set('')
                    self.question_c.set('')
                    self.question_d.set('')
            else:
                data = self.question_bank1()
                if self.count != 0:
                    self.count -= 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])
                    self.question_a.set('')
                    self.question_b.set('')
                    self.question_c.set('')
                    self.question_d.set('')
        else:
            if self.mode_choose.get() == 'A':
                data = self.question_bank()
                if self.count != 0:
                    self.count -= 1
                    print(self.count)
                    self.questions.set(data[self.count-1][0])
                    self.question_select_a.configure(text=data[self.count-1][1])
                    self.question_select_b.configure(text=data[self.count-1][2])
                    self.question_select_c.configure(text=data[self.count-1][3])
                    self.question_select_d.configure(text=data[self.count-1][4])
                    self.option.set('')
            else:
                data = self.question_bank()
                if self.count != 0:
                    self.count -= 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])
                    self.option.set('')

    def jump_question(self):
        if self.more_than_one.get() == "O":
            self.option.set('')
            self.display_anwser_label.configure(text="答案为:")
            for i in range(1, len(self.question_bank())+1):
                if self.box[i].get() != self.number[i-1]:
                    self.number[i-1] = self.box[i].get()
                    value = self.box[i].get()
                    self.count = value - 1
                    print(self.count)
                    data = self.question_bank()
                    self.box[i].set(0)
                    self.number[i - 1] = self.box[i].get()
                    if value != 0:
                        self.questions.set(data[value-1][0])
                        print(value)
                        self.question_select_a.configure(text=data[value - 1][1])
                        print(value)
                        self.question_select_b.configure(text=data[value - 1][2])
                        self.question_select_c.configure(text=data[value - 1][3])
                        self.question_select_d.configure(text=data[value - 1][4])
                        break
        else:
            self.question_a.set('')
            self.question_b.set('')
            self.question_c.set('')
            self.question_d.set('')
            self.display_anwser_label.configure(text="答案为:")
            for i in range(1, len(self.question_bank1()) + 1):
                if self.box[i].get() != self.number[i-1]:
                    self.number[i - 1] = self.box[i].get()
                    value = self.box[i].get()
                    self.count = value - 1
                    data = self.question_bank1()
                    self.box[i].set(0)
                    self.number[i - 1] = self.box[i].get()
                    if value != 0:
                        self.questions.set(data[value - 1][0])
                        self.question_select_a.configure(text=data[value - 1][1])
                        self.question_select_b.configure(text=data[value - 1][2])
                        self.question_select_c.configure(text=data[value - 1][3])
                        self.question_select_d.configure(text=data[value - 1][4])
                        break

    def next_page(self):
        self.display_anwser_label.configure(text="答案为:")
        if self.mode_choose.get() == 'A':
            if self.more_than_one.get() == 'M':
                data = self.question_bank1()
                if self.count != len(data)-1:
                    self.count += 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])
                    self.question_a.set('')
                    self.question_b.set('')
                    self.question_c.set('')
                    self.question_d.set('')
            else:
                data = self.question_bank()
                if self.count != len(data) - 1:
                    self.count += 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])
                    self.option.set('')
        else:
            if self.more_than_one.get() == 'M':
                data = self.question_bank1()
                self.question_a.set('')
                self.question_b.set('')
                self.question_c.set('')
                self.question_d.set('')
                if self.count != len(data) - 1:
                    self.count += 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])
            else:
                data = self.question_bank()
                self.option.set('')
                if self.count != len(data) - 1:
                    self.count += 1
                    self.questions.set(data[self.count][0])
                    self.question_select_a.configure(text=data[self.count][1])
                    self.question_select_b.configure(text=data[self.count][2])
                    self.question_select_c.configure(text=data[self.count][3])
                    self.question_select_d.configure(text=data[self.count][4])

    def question_answer(self):
        print(self.count)
        self.answer.clear()
        praise = ["You're so smart", "You're so intelligent", "You're so knowledgeable", "You're so clever"]
        encourge = ["You still have to study hard", "You still have to work harder", "You should take study to heart",
                    "You should put your energy on your study"]
        if self.more_than_one.get() == "O":
            self.answer.append(self.option.get())
            answer = ''.join(self.answer)
            if self.mode_choose.get() == 'A':
                judgment = (answer == self.question_bank()[self.count][5] and self.serial_number[self.count] != 0)
                judgment1 = (answer != self.question_bank()[self.count][5] and self.serial_number[self.count] != 0)
                judgment2 = (self.serial_number[self.count] == 0 and answer != self.question_bank()[self.count][5])
                judgment3 = (self.serial_number[self.count] == 0 and answer == self.question_bank()[self.count][5])
            else:
                judgment = (answer == self.question_bank()[self.count][5] and self.serial_number[self.count] != 0)
                judgment1 = (answer != self.question_bank()[self.count][5] and self.serial_number[self.count] != 0)
                judgment2 = (self.serial_number[self.count] == 0 and answer != self.question_bank()[self.count][5])
                judgment3 = (self.serial_number[self.count] == 0 and answer == self.question_bank()[self.count][5])
            if len(answer) != 0:
                self.number_question_number.append(self.compute)
                if judgment:
                    if self.mode_choose.get() == 'A':
                        self.display_anwser_label.configure(text="答案为:" + self.question_bank()[self.count][5])
                        self.serial_number[self.count] = 0
                        self.scores += 1
                        self.box[self.count + 1].set(self.count + 1)
                        self.number[self.count] = self.count + 1
                    elif self.mode_choose.get() == 'B':
                        self.display_anwser_label.configure(
                            text=praise[random.randint(0, 3)] + "  答案为:" + self.question_bank()[self.count][5])
                elif judgment1:
                    if self.mode_choose.get() == 'A':
                        self.display_anwser_label.configure(
                            text="答案为:" + self.question_bank()[self.count][5])
                        self.serial_number[self.count] = 0
                        self.box[self.count + 1].set(self.count + 1)
                        self.number[self.count] = self.count + 1
                    elif self.mode_choose.get() == 'B':
                        self.display_anwser_label.configure(
                            text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank()[self.count][5])
                elif judgment2:
                    if self.scores != 0:
                        if self.mode_choose.get() == 'A':
                            self.display_anwser_label.configure(text="答案为:" + self.question_bank()[self.count][5])
                            self.scores -= 1
                            self.serial_number[self.count] = self.count + 1
                            self.box[self.count + 1].set(self.count + 1)
                            self.number[self.count] = self.count + 1
                        elif self.mode_choose.get() == 'B':
                            self.display_anwser_label.configure(
                                text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank()[self.count][
                                    5])
                elif judgment3:
                    if self.scores < len(self.serial_number):
                        if self.mode_choose.get() == 'A':
                            self.display_anwser_label.configure(text="答案为:" + self.question_bank()[self.count][5])
                            self.scores += 1
                            self.box[self.count + 1].set(self.count + 1)
                            self.number[self.count] = self.count + 1
                        elif self.mode_choose.get() == 'B':
                            self.display_anwser_label.configure(
                                text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank()[self.count][5])
                else:
                    if self.mode_choose.get() == 'A':
                        self.box[self.count + 1].set(self.count + 1)
                        self.number[self.count] = self.count + 1
                        self.display_anwser_label.configure(text="答案为:" + self.question_bank()[self.count][5])
                    elif self.mode_choose.get() == 'B':
                        self.display_anwser_label.configure(
                            text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank()[self.count][5])
            elif len(answer) == 0:
                messagebox.showinfo('答题小程序', '请选择您的答案')
            else:
                self.number_question_number.append(0)
            if len([i for i in self.serial_number if i == 0]) == len(self.question_bank()) \
                    and self.count == len(self.question_bank()) - 1:
                messagebox.showinfo('答题小程序', '答题完成')
        if self.more_than_one.get() == "M":
            if self.question_a.get() == '1':
                self.answer.append('A')
            if self.question_b.get() == '1':
                self.answer.append('B')
            if self.question_c.get() == '1':
                self.answer.append('C')
            if self.question_d.get() == '1':
                self.answer.append('D')
            answer = ''.join(self.answer)
            if self.mode_choose.get() == 'A':
                judgment = (answer == self.question_bank1()[self.count][5] and self.serial_number[self.count] != 0)
                judgment1 = (answer != self.question_bank1()[self.count][5] and self.serial_number[self.count] != 0)
                judgment2 = (self.serial_number[self.count] == 0 and answer != self.question_bank1()[self.count][5])
                judgment3 = (self.serial_number[self.count] == 0 and answer == self.question_bank1()[self.count][5])
            else:
                judgment = (answer == self.question_bank1()[self.count][5] and self.serial_number[self.count] != 0)
                judgment1 = (answer != self.question_bank1()[self.count][5] and self.serial_number[self.count] != 0)
                judgment2 = (self.serial_number[self.count] == 0 and answer != self.question_bank1()[self.count][5])
                judgment3 = (self.serial_number[self.count] == 0 and answer == self.question_bank1()[self.count][5])
            if len(answer) != 0:
                self.number_question_number.append(self.compute)
                if judgment:
                    if self.mode_choose.get() == 'A':
                        self.display_anwser_label.configure(text="答案为:" + self.question_bank1()[self.count][5])
                        self.serial_number[self.count] = 0
                        self.scores += 1
                        self.box[self.count + 1].set(self.count + 1)
                        self.number[self.count] = self.count + 1
                    elif self.mode_choose.get() == 'B':
                        self.display_anwser_label.configure(
                            text=praise[random.randint(0, 3)] + "  答案为:" + self.question_bank1()[self.count][5])
                elif judgment1:
                    if self.mode_choose.get() == 'A':
                        self.display_anwser_label.configure(
                            text="答案为:" + self.question_bank1()[self.count][5])
                        self.serial_number[self.count] = 0
                        self.box[self.count + 1].set(self.count + 1)
                        self.number[self.count] = self.count + 1
                    elif self.mode_choose.get() == 'B':
                        self.display_anwser_label.configure(
                            text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank1()[self.count][5])
                elif judgment2:
                    if self.scores != 0:
                        if self.mode_choose.get() == 'A':
                            self.display_anwser_label.configure(text="答案为:" + self.question_bank1()[self.count][5])
                            self.scores -= 1
                            self.serial_number[self.count] = self.count + 1
                            self.box[self.count + 1].set(self.count + 1)
                            self.number[self.count] = self.count + 1
                        elif self.mode_choose.get() == 'B':
                            self.display_anwser_label.configure(
                                text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank1()[self.count][5])
                elif judgment3:
                    if self.scores < len(self.serial_number):
                        if self.mode_choose.get() == 'A':
                            self.display_anwser_label.configure(text="答案为:" + self.question_bank1()[self.count][5])
                            self.scores += 1
                            self.box[self.count + 1].set(self.count + 1)
                            self.number[self.count] = self.count + 1
                        elif self.mode_choose.get() == 'B':
                            self.display_anwser_label.configure(
                                text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank1()[self.count][5])
                else:
                    if self.mode_choose.get() == 'A':
                        self.box[self.count + 1].set(self.count + 1)
                        self.number[self.count] = self.count + 1
                        self.display_anwser_label.configure(text="答案为:" + self.question_bank1()[self.count][5])
                    elif self.mode_choose.get() == 'B':
                        self.display_anwser_label.configure(
                            text=encourge[random.randint(0, 3)] + "  答案为:" + self.question_bank1()[self.count][5])
            elif len(answer) == 0:
                messagebox.showinfo('答题小程序', '请选择您的答案')
            else:
                self.number_question_number.append(0)
            if len([i for i in self.serial_number if i == 0]) == len(self.question_bank1()) \
                    and self.count == len(self.question_bank1()) - 1:
                messagebox.showinfo('答题小程序', '答题完成')

    def sign_in(self):
        if len(self.username_entry1.get()) == 0:
            self.result.configure(text='请输入账号')
        elif len(self.username_entry1.get()) < 7:
            self.result.configure(text='账号输入错误')
        elif len(self.username_entry1.get()) != 0 and len(self.password_entry1.get()) == 0:
            self.result.configure(text='请输入密码')
        elif len(self.username_entry1.get()) != 0 and len(self.password_entry1.get()) <= 4:
            self.result.configure(text='密码位数不足四位')
        elif len(self.username_entry1.get()) != 0 and len(self.password_entry1.get()) != 0 and \
                len(self.password_entry2.get()) == 0:
            self.result.configure(text='请输入确认密码')
        elif len(self.sign_data()) == 0 and len(self.username_entry1.get()) != 0 \
                and len(self.password_entry1.get()) != 0 and self.password_entry1.get().isdigit() or \
                self.password_entry2.get().isdigit():
            self.result.configure(text='密码不能只由数字或者字母构成')
        elif len(self.sign_data()) == 0 and len(self.username_entry1.get()) != 0 \
                and len(self.password_entry1.get()) != 0 and self.password_entry1.get() != self.password_entry2.get():
            self.result.configure(text='密码不一致')
        elif len(self.sign_data()) == 0 and len(self.username_entry1.get()) != 0 \
                and len(self.password_entry1.get()) != 0 and self.password_entry1.get() == self.password_entry2.get():
            coon = sqlite3.connect(self.item_bank)
            cur = coon.cursor()
            cur.execute("insert into sign(username, password)values(?, ?)", (self.username_entry1.get(),
                                                                             self.password_entry1.get()))
            coon.commit()
            self.result.configure(text='账号注册成功')
        else:
            for i in range(len(self.sign_data())):
                if self.username_entry1.get() == self.sign_data()[i][0]:
                    self.result.configure(text='账号已存在')
                elif i == len(self.sign_data())-1 and self.username_entry1.get() != self.sign_data()[i][0]:
                    if self.password_entry1.get() == self.password_entry2.get():
                        coon = sqlite3.connect(self.item_bank)
                        cur = coon.cursor()
                        cur.execute("insert into sign(username, password)values(?, ?)", (self.username_entry1.get(),
                                                                                         self.password_entry1.get()))
                        coon.commit()
                        self.result.configure(text='账号注册成功')
                    elif self.password_entry1.get() != self.password_entry2.get():
                        self.result.configure(text='密码不一致')
                        self.password_entry1.delete(0, END)
                        self.password_entry2.delete(0, END)
                    else:
                        self.username_entry1.delete(0, END)
                        self.password_entry1.delete(0, END)
                        self.password_entry2.delete(0, END)
                        self.result.configure(text='注册失败,请重新注册')

    def registered_account(self):
        self.panedwindow.grid_forget()
        self.panedwindow1 = PanedWindow(master=self.window_name, orient='vertical')
        self.panedwindow1.grid(row=0, column=0)
        title_frame1 = ttk.Frame(master=self.panedwindow1, width=self.width, height=90)
        self.panedwindow1.add(title_frame1)
        sign_frame1 = ttk.Frame(self.panedwindow1)
        self.panedwindow1.add(sign_frame1)
        choose_day_frame1 = ttk.Frame(self.panedwindow1)
        self.panedwindow1.add(choose_day_frame1)
        title_frame1.pack()
        sign_frame1.pack()
        choose_day_frame1.pack()
        # 注册账号组件创建
        title = Label(title_frame1, width=self.width, height=90, image=self.photo)
        title.grid()
        username1 = ttk.Label(sign_frame1, text='账号:', font=("华文新魏", 13))
        username_v1 = StringVar()
        self.username_entry1 = ttk.Entry(sign_frame1, textvariable=username_v1, font=("华文新魏", 13), validate='key',
                                         validatecommand=(self.username_validate, "%P"))
        password1 = ttk.Label(sign_frame1, text='密  码:', font=("华文新魏", 13))
        password_v1 = StringVar()
        self.password_entry1 = ttk.Entry(sign_frame1, textvariable=password_v1, font=("华文新魏", 13), show='.',
                                         validate='key', validatecommand=(self.password_validate, '%P'))
        password2 = ttk.Label(sign_frame1, text='确认密码:', font=("华文新魏", 13))
        password_v2 = StringVar()
        self.password_entry2 = ttk.Entry(sign_frame1, textvariable=password_v2, font=("华文新魏", 13), show='.',
                                         validate='key', validatecommand=(self.password_validate, '%P'))
        self.result = ttk.Label(choose_day_frame1, text='', font=("华文新魏", 11))
        sign = ttk.Button(choose_day_frame1, text='确认注册', command=self.sign_in)
        quit_sign = ttk.Button(choose_day_frame1, text='退出注册', command=self.quit_sign_in)
        username1.grid(row=0, column=1, padx=(35, 10), pady=0)
        self.username_entry1.grid(row=0, column=2, padx=14, pady=10)
        password1.grid(row=1, column=1, padx=(35, 10), pady=10)
        self.password_entry1.grid(row=1, column=2, padx=14, pady=10)
        password2.grid(row=2, column=1, padx=(15, 10), pady=10)
        self.password_entry2.grid(row=2, column=2, padx=14, pady=1)
        self.result.grid(row=0, column=0, columnspan=3, padx=(20, 0), pady=1)
        sign.grid(row=1, column=0, padx=(20, 0), ipadx=30)
        quit_sign.grid(row=1, column=1,  padx=10, ipadx=30)

    def find_password(self):
        self.panedwindow.grid_forget()
        self.panedwindow2 = PanedWindow(master=self.window_name, orient='vertical')
        self.panedwindow2.grid(row=0, column=0)
        title_frame2 = ttk.Frame(master=self.panedwindow2, width=self.width, height=90)
        self.panedwindow2.add(title_frame2)
        sign_frame2 = ttk.Frame(self.panedwindow2)
        self.panedwindow2.add(sign_frame2)
        choose_day_frame2 = ttk.Frame(self.panedwindow2)
        self.panedwindow2.add(choose_day_frame2)
        result_frame = ttk.Frame(self.panedwindow2)
        self.panedwindow2.add(result_frame)
        title_frame2.pack()
        sign_frame2.pack()
        choose_day_frame2.pack()
        result_frame.pack()
        # 找回密码组件创建
        title1 = Label(title_frame2, width=self.width, height=90, image=self.photo)
        title1.grid(row=0, column=0)
        username2 = ttk.Label(sign_frame2, text='账号:', font=("华文新魏", 13))
        username_v2 = StringVar()
        self.username_entry2 = ttk.Entry(sign_frame2, textvariable=username_v2, font=("华文新魏", 13), validate='key',
                                         validatecommand=(self.username_validate, '%P'))
        password3 = ttk.Label(sign_frame2, text='服务密码:', font=("华文新魏", 13))
        password_v3 = StringVar()
        self.password_entry3 = ttk.Entry(sign_frame2, textvariable=password_v3, font=("华文新魏", 13), show='.',
                                         validate='key', validatecommand=(self.password_validate, '%P'))
        find = ttk.Button(choose_day_frame2, text='找回密码', command=self.find_it)
        quit_find = ttk.Button(choose_day_frame2, text=' 退 出 ', command=self.quit_find)
        self.result3 = ttk.Label(result_frame, text='', font=("华文新魏", 13))
        username2.grid(row=0, column=1, padx=(40, 10), pady=0)
        self.username_entry2.grid(row=0, column=2, padx=14, pady=10)
        password3.grid(row=1, column=1, padx=(10, 10), pady=10)
        self.password_entry3.grid(row=1, column=2, padx=14, pady=10)
        find.grid(row=0, column=0, padx=(2, 40), ipadx=20)
        quit_find.grid(row=0, column=1, padx=(10, 0), ipadx=20)
        self.result3.pack()

    def cancel_account(self):
        self.panedwindow.grid_forget()
        self.panedwindow3 = PanedWindow(master=self.window_name, orient='vertical')
        self.panedwindow3.grid(row=0, column=0)
        title_frame3 = ttk.Frame(master=self.panedwindow3, width=self.width, height=90)
        self.panedwindow3.add(title_frame3)
        sign_frame3 = ttk.Frame(self.panedwindow3)
        self.panedwindow3.add(sign_frame3)
        result_frame = ttk.Frame(self.panedwindow3)
        self.panedwindow3.add(result_frame)
        choose_day_frame3 = ttk.Frame(self.panedwindow3)
        self.panedwindow3.add(choose_day_frame3)
        title_frame3.pack()
        sign_frame3.pack()
        result_frame.pack()
        choose_day_frame3.pack()
        # 注销密码组件创建
        title2 = Label(title_frame3, width=self.width, height=90, image=self.photo)
        title2.grid()
        username3 = ttk.Label(sign_frame3, text='账号:', font=("华文新魏", 13))
        username_v3 = StringVar()
        self.username_entry3 = ttk.Entry(sign_frame3, textvariable=username_v3, font=("华文新魏", 13), validate='key',
                                         validatecommand=(self.username_validate, '%P'))
        password4 = ttk.Label(sign_frame3, text='密码:', font=("华文新魏", 13))
        password_v4 = StringVar()
        self.password_entry4 = ttk.Entry(sign_frame3, textvariable=password_v4, font=("华文新魏", 13), show='.',
                                         validate='key', validatecommand=(self.password_validate, '%P'))
        self.result1 = ttk.Label(result_frame, text='', font=("华文新魏", 13))
        account = ttk.Button(choose_day_frame3, text='注销账号', command=self.cancel)
        quit_account = ttk.Button(choose_day_frame3, text='退出注销', command=self.quit_account)
        username3.grid(row=0, column=1, padx=(15, 10), pady=0)
        self.username_entry3.grid(row=0, column=2, padx=14, pady=10)
        password4.grid(row=1, column=1, padx=(15, 10), pady=10)
        self.password_entry4.grid(row=1, column=2, padx=14, pady=10)
        self.result1.pack()
        account.grid(row=0, column=0, padx=(10, 0), ipadx=20)
        quit_account.grid(row=0, column=1, padx=(25, 0), ipadx=20)

    def change(self):
        self.panedwindow.grid_forget()
        self.panedwindow4 = PanedWindow(master=self.window_name, orient='vertical')
        self.panedwindow4.grid(row=0, column=0)
        title_frame4 = ttk.Frame(master=self.panedwindow4, width=self.width, height=90)
        self.panedwindow4.add(title_frame4)
        sign_frame4 = ttk.Frame(self.panedwindow4)
        self.panedwindow4.add(sign_frame4)
        choose_day_frame4 = ttk.Frame(self.panedwindow4)
        self.panedwindow4.add(choose_day_frame4)
        title_frame4.pack()
        sign_frame4.pack()
        choose_day_frame4.pack()
        # 修改密码组件创建
        title = Label(title_frame4, width=self.width, height=90, image=self.photo)
        title.grid()
        username1 = ttk.Label(sign_frame4, text='账号:', font=("华文新魏", 13))
        username_v1 = StringVar()
        self.username_entry4 = ttk.Entry(sign_frame4, textvariable=username_v1, font=("华文新魏", 13), validate='key',
                                         validatecommand=(self.username_validate, '%P'))
        password1 = ttk.Label(sign_frame4, text='原始密码:', font=("华文新魏", 13))
        password_v1 = StringVar()
        self.password_entry5 = ttk.Entry(sign_frame4, textvariable=password_v1, font=("华文新魏", 13), show='.',
                                         validate='key', validatecommand=(self.password_validate, '%P'))
        password2 = ttk.Label(sign_frame4, text='确认密码:', font=("华文新魏", 13))
        password_v2 = StringVar()
        self.password_entry6 = ttk.Entry(sign_frame4, textvariable=password_v2, font=("华文新魏", 13), validate='key',
                                         validatecommand=(self.password_validate, '%P'))
        self.result2 = ttk.Label(choose_day_frame4, text='', font=("华文新魏", 11))
        sign = ttk.Button(choose_day_frame4, text='确认修改', command=self.confirm_modification)
        quit_sign = ttk.Button(choose_day_frame4, text='退出修改', command=self.quit_change)
        username1.grid(row=0, column=1, padx=(50, 5), pady=0)
        self.username_entry4.grid(row=0, column=2, padx=14, pady=10)
        password1.grid(row=1, column=1, padx=(15, 5), pady=10)
        self.password_entry5.grid(row=1, column=2, padx=14, pady=10)
        password2.grid(row=2, column=1, padx=(15, 5), pady=10)
        self.password_entry6.grid(row=2, column=2, padx=14, pady=1)
        self.result2.grid(row=0, column=0, columnspan=3, padx=(20, 0), pady=1)
        sign.grid(row=1, column=0, padx=(20, 0), ipadx=30)
        quit_sign.grid(row=1, column=1, padx=10, ipadx=30)

    def cancel(self):
        if len(self.username_entry3.get()) == 0:
            self.result1.configure(text='请输入账号')
        elif len(self.username_entry3.get()) < 7:
            self.result1.configure(text='账号输入错误')
        elif len(self.username_entry3.get()) != 0 and len(self.password_entry4.get()) == 0:
            self.result1.configure(text='请输入密码')
        else:
            for i in range(len(self.sign_data())):
                if self.username_entry3.get() == self.sign_data()[i][0] and self.password_entry4.get() == \
                        self.sign_data()[i][1]:
                    con = sqlite3.connect(self.item_bank)
                    cur = con.cursor()
                    cur.execute('delete from sign where username=?', (self.username_entry3.get(),))
                    con.commit()
                    self.result1.configure(text='账号注销成功')
                    break
                elif self.username_entry3.get() == self.sign_data()[i][0] and self.password_entry4.get() != \
                        self.sign_data()[i][1] and len(self.password_entry4.get()):
                    self.result1.configure(text='密码错误')
                    break
                elif i == len(self.sign_data())-1 and self.username_entry3.get() != self.sign_data()[i][0]:
                    self.result1.configure(text='该账号不存在')

    def sign_up(self):
        if len(self.sign_data()) == 0:
            self.username_v.set('请进行账号注册')
        elif self.username_entry.get() == 0:
            self.username_v.set('请输入账号')
        elif len(self.username_entry.get()) < 7:
            self.username_v.set('账号输入错误')
        elif len(self.password_entry.get()) == 0:
            self.password_v.set('请输入密码')
            self.password_entry.configure(show='', background='grey')
        else:
            for i in range(len(self.sign_data())):
                if self.username_entry.get() == self.sign_data()[i][0] and self.password_entry.get() == \
                        self.sign_data()[i][1]:
                    self.update_memory()
                    self.creat_window()
                    break
                elif self.username_entry.get() == self.sign_data()[i][0] and self.password_entry.get() != \
                        self.sign_data()[i][1]:
                    self.password_v.set('密码错误')
                    self.password_entry.configure(show='', background='grey')
                    break
                elif i == len(self.sign_data())-1 and self.username_entry.get() != self.sign_data()[i][0]:
                    self.username_v.set('账号不存在')

    def find_it(self):
        if len(self.username_entry2.get()) < 7:
            self.result3.configure(text='账号输入错误')
        elif len(self.username_entry2.get()) == 0:
            self.result3.configure(text='请输入账号')
        elif len(self.password_entry3.get()) == 0:
            self.result3.configure(text='请输入服务密码')
        else:
            for i in range(len(self.sign_data())):
                if self.username_entry2.get() == self.sign_data()[i][0] and self.password_entry3.get() == \
                        self.code_data()[0][1]:
                    self.result3.configure(text='您的密码是: {0}'.format(self.sign_data()[i][1]))
                    break
                elif self.username_entry2.get() == self.sign_data()[i][0] and self.password_entry3.get() != \
                        self.code_data()[0][1]:
                    self.result3.configure(text='服务密码错误')
                    self.username_entry2.delete(0, END)
                    self.password_entry3.delete(0, END)
                    break
                elif i == len(self.sign_data())-1 and self.username_entry2.get() != self.sign_data()[i][0]:
                    self.result3.configure(text='账号不存在')
                    self.username_entry2.delete(0, END)
                    self.password_entry3.delete(0, END)
                    break

    def confirm_modification(self):
        if len(self.username_entry4.get()) == 0:
            self.result2.configure(text='请输入账号')
        elif len(self.username_entry4.get()) < 7:
            self.result2.configure(text='账号输入错误')
        elif len(self.username_entry4.get()) != 0 and len(self.password_entry5.get()) == 0:
            self.result2.configure(text='请输入原始密码')
        elif len(self.username_entry4.get()) != 0 and len(self.password_entry5.get()) != 0 and \
                len(self.password_entry6.get()) == 0:
            self.result2.configure(text='修改密码不能为空')
        elif len(self.username_entry4.get()) != 0 and len(self.password_entry5.get()) != 0 and \
                len(self.password_entry6.get()) <= 4:
            self.result2.configure(text='修改密码不足四位')
        else:
            for i in range(len(self.sign_data())):
                if self.username_entry4.get() == self.sign_data()[i][0]:
                    if self.password_entry6.get().isdigit():
                        self.result2.configure(text='密码不能只由数字或字母构成')

                    elif self.password_entry5.get() == self.sign_data()[i][1]:
                        coon = sqlite3.connect(self.item_bank)
                        cur = coon.cursor()
                        cur.execute('update sign set password=? where username=?', (self.password_entry6.get(),
                                                                                    self.username_entry4.get()))
                        coon.commit()
                        self.result2.configure(text='密码修改成功')
                    elif i == len(self.sign_data())-1 and self.password_entry5.get() != self.sign_data()[i][1]:
                        self.result2.configure(text='原始密码错误')
                        self.password_entry5.delete(0, END)
                else:
                    self.result2.configure(text='账号不存在')

    def quit_change(self):
        self.panedwindow4.grid_forget()
        self.panedwindow.grid(row=0, column=0)

    def on_closing(self):
        self.window.destroy()
        self.window_name.destroy()

    def quit(self):
        self.window.destroy()
        self.compute = 1
        self.window_name.deiconify()

    def get_score(self):
        if self.more_than_one.get() == 'M':
            if self.count == len(self.question_bank1())-1 and \
                    len([i for i in self.serial_number if i == 0]) == len(self.question_bank1()) \
                    or len([i for i in self.number if i != 0]) == len(self.question_bank1()):
                for i in range(len(self.number_question_number)):
                    if self.number_question_number[i] != 0 and i == len(self.number_question_number)-1 or\
                            len([i for i in self.number if i != 0]):
                        if messagebox.askquestion('答题小程序', '确认提交成绩'):
                            self.score.configure(text='得分:{0}分'.format(10 * self.scores))
                            break
                    elif self.number_question_number[i] == 0:
                        messagebox.showinfo('答题小程序', '答题未完成')
                        break
            else:
                messagebox.showinfo('答题小程序', '答题未完成')
        else:
            if self.count == len(self.question_bank()) - 1 and \
                    len([i for i in self.serial_number if i == 0]) == len(self.question_bank()) \
                    or len([i for i in self.number if i != 0]) == len(self.question_bank()):
                for i in range(len(self.number_question_number)):
                    if self.number_question_number[i] != 0 and i == len(self.number_question_number) - 1 or \
                            len([i for i in self.number if i != 0]):
                        if messagebox.askquestion('答题小程序', '确认提交成绩'):
                            self.score.configure(text='得分:{0}分'.format(10 * self.scores))
                            break
                    elif self.number_question_number[i] == 0:
                        messagebox.showinfo('答题小程序', '答题未完成')
                        break
            else:
                messagebox.showinfo('答题小程序', '答题未完成')

    def change_bank(self, event):
        self.item_bank = "./" + self.bank_question.get()
        self.mode_choose.set('A')
        self.more_than_one.set('O')
        self.display_box()
        self.reset()
        self.window_name.update()
        print(event)

    def font(self, event):
        self.question.config(
            font=(self.choose_font_family1.get(), int(self.choose_font_family3.get()), self.choose_font_family2.get())
        )
        style = ttk.Style()
        style.configure('my.TCheckbutton', font=(self.choose_font_family1.get(), int(self.choose_font_family3.get()),
                                                 self.choose_font_family2.get()), height=100)
        style = ttk.Style()
        style.configure('my.TRadiobutton', font=(self.choose_font_family1.get(), int(self.choose_font_family3.get()),
                                                 self.choose_font_family2.get()), height=100)
        self.window.update()
        print(event)

    def reset(self):
        if self.more_than_one.get() == 'O':
            data = self.question_bank()
            self.option.set('')
        else:
            data = self.question_bank1()
        self.display_anwser_label.configure(text="答案为:")
        if self.mode_choose.get() == 'A':
            self.count = 0
            self.compute = 1
            self.scores = 0
            self.serial_number = [i for i in range(1, len(data) + 1)]
            self.score.configure(text='得分:')
            for i in range(len(data)):
                self.box[i+1].set(0)
            self.question_a.set('')
            self.question_b.set('')
            self.question_c.set('')
            self.question_d.set('')
            self.number = [i*0 for i in range(len(self.question_bank()))]
            data = self.question_bank()
            self.questions.set(data[self.count][0])
            self.question_select_a.configure(text=data[self.count][1])
            self.question_select_b.configure(text=data[self.count][2])
            self.question_select_c.configure(text=data[self.count][3])
            self.question_select_d.configure(text=data[self.count][4])
        else:
            self.count = 0
            self.compute = 1
            self.scores = 0
            self.serial_number = [i for i in range(1, len(self.question_bank1()) + 1)]
            self.score.configure(text='得分:')
            for i in range(len(self.question_bank1())):
                self.box[i + 1].set(0)
            self.question_a.set('')
            self.question_b.set('')
            self.question_c.set('')
            self.question_d.set('')
            self.number = [i * 0 for i in range(len(self.question_bank1()))]
            data = self.question_bank1()
            self.questions.set(data[self.count][0])
            self.question_select_a.configure(text=data[self.count][1])
            self.question_select_b.configure(text=data[self.count][2])
            self.question_select_c.configure(text=data[self.count][3])
            self.question_select_d.configure(text=data[self.count][4])

    def pop(self, event):
        self.menu.post(event.x_root, event.y_root)

    def callback_one(self):
        self.username_entry.event_generate('<<Cut>>')

    def callback_two(self):
        self.username_entry.event_generate('<<Copy>>')

    def callback_three(self):
        self.username_entry.event_generate('<<Paste>>')

    def sign_down(self, event):
        self.window_name.update()
        self.sign_up()
        print(event)

    def quit_account(self):
        self.panedwindow3.grid_forget()
        self.panedwindow.grid(row=0, column=0)

    def quit_sign_in(self):
        self.panedwindow1.grid_forget()
        self.panedwindow.grid(row=0, column=0)

    def quit_find(self):
        self.panedwindow2.grid_forget()
        self.panedwindow.grid(row=0, column=0)

    def callback_four(self):
        self.window_name.update()

    def callback_frist(self, event):
        print(event)
        self.callback_one()

    def callback_second(self, event):
        print(event)
        self.callback_two()

    def callback_third(self, event):
        print(event)
        self.callback_three()

    def callback_fourth(self, event):
        print(event)
        self.callback_four()


if __name__ == "__main__":
    root = Tk()
    answer_question = AnswerQuestion(root)
    answer_question.menory_function()
    root.mainloop()
