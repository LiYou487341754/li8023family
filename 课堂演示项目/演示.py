# 以下是Python代码示例：
#
# ```
from tkinter import *

root = Tk()

# 定义一个列表，包含所有的选项
options = ["选项1", "选项2", "选项3", "选项4", "选项5"]

# 定义一个字典，用于存储每个Checkbutton的值
checked = {}

# 创建Checkbutton函数


def create_checkbutton(option):
    checked[option] = BooleanVar()
    checked[option].set(False)
    cb = Checkbutton(root, text=option, variable=checked[option], command=lambda: print_checked(option))
    cb.pack()

# 创建打印选中值函数


def print_checked(option):
    if checked[option].get():
        print(option)

# 循环创建Checkbutton

for option in options:
    create_checkbutton(option)

root.mainloop()
# ```
#
# 上述代码通过循环遍历选项列表，创建每个选项的Checkbutton，并将其绑定到对应的BooleanVar对象和打印选中值的函数，以便在用户点击时打印出其值。