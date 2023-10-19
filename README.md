# 链式赋值
x = y = 10
print("x = {0}\ny = {1}".format(x, y))

# 系列解包赋值
a, b, c = 10, 20, 30
print("a = {0}\nb = {1}\nc = {2}".format(a, b, c))

# 常量
PI = 3.14
R = int(input("请输入圆的半径:"))
area = PI * R * R
print("area={:.2f}".format(area))

# divmod()同时得到商和余数,返回为元组
e = divmod(4, 3)
print("商和余数:", e)

# 进制函数
# 二进制
two = bin(a)
print("二进制:", two)
# 八进制
eight = oct(a)
print("八进制:", eight)
# 十六进制
sexteen = hex(a)
print("十六进制:", sexteen)

# 布尔值
boolean = bool(a)
print(boolean)

# 字符串的编码
# 内置函数 ord()可以把字符转换成对应的 Unicode 码
A = ord("黎")
print(A)
# 内置函数 chr()可以把十进制数字转换成对应的字符
B = chr(100)
print(B)

# 不换行打印
print("姓名:", end='')
print("-------", end='>')
print("黎杰")

# 插入打印
print("黎杰", "重庆人文科技学院", sep="毕业于")

# 数据类型转换字符类型
number = 5.20
str_number = str(number)
print(type(number), number, sep='--------->', end='\n')
print(type(str_number), str_number, sep='--------->', end='\n')

# 使用[]提取字符串中字符
str_letter = 'abcdefghijklmnopqrstuvwxyz'
len_letter = len(str_letter)  # 获取字符串长度
print('总字母数:', len_letter, end='\n')
# 正向提取:第一个字符,偏移量是0, 最后一个字符,偏移量是len(str_letter)-1
print("正向提取:\n", "\t第一个字母:", str_letter[0], end='\t')
print("最后一个字母:", str_letter[len_letter-1], end='\n')
# 反向提取:第一个字符,偏移量是-1， 最后一个字符,偏移量是-len(str_letter)
print("反向提取:\n", "\t第一个字母:", str_letter[-1], end='\t')
print("最后一个字母:", str_letter[-len_letter])

# replace()实现字符串替换,创建新的字符串对象
new_letter = str_letter.replace('c', '黎')
print("原始对象:", str_letter)
print("新对象:", new_letter)

# 字符串切片slice操作,包头不包尾

print("切片操作:")
print(str_letter[:])  # 提取整个字符串
print(str_letter[2:])  # 从索引2位置开始提取字符串
print(str_letter[:2])  # 从头开始到索引2位置
print(str_letter[2:4])  # 提取从索引2位置开始到索引4-1位置结束
print(str_letter[1:24:2])  # 提取从索引1位置开始到24-1位置结束,步长为2
print(str_letter[-3:])  # 倒数3个
print(str_letter[-8:-2])  # 倒数第8个到倒数第3个
print(str_letter[::-1])  # 步长为负,从右到左反向提取

# 将"to be or not to be"字符串倒序输出
output_str = 'to be or not to be'
print(output_str[::-1])

#  将”sxtsxtsxtsxtsxt“字符串中所有的 s 输出
output = 'sxtsxtsxtsxtsxt'
print(output[::3])

# split()分割
output = output_str.split()
print(output_str.split("or"))  # 基于指定分隔符将字符串分隔成多个子字符串(存储列表中)
print(output)  # 无指定分隔符,则默认使用空白字符(换行符/空格/制表符)
print(output_str)

# join()合并
print(" ".join(output))
print("*".join(output))

# 字符串驻留机制
# 仅保存一份相同不可变字符串的方法,不同的值被放在字符串驻留池中,[对于符合标识符规则的字符串
# (仅包含下划线(_)、字母、数字)交互模式下会启用字符串驻留机制],字符串只在编译时驻留，而非运行时
a = 'abd_33'
b = 'abd_33'
print(a is b)
c = 'li##'
d = 'li##'
print(c is d)
print(id(c))
print(id(d))
str1 = 'li'
str2 = 'jie'
# str1+str2 is 'lijie'

# 比较使用'=='和'!='
print(str1 == str2)
print(str1 != str2)
print(str2)
print(str1 + str2 == 'lijie')
print(str2 + str2 != 'lijie')

# 判断是否为同一对象 is / is not 比较的是id值
print(a is b)
print(a is not b)

# 是否存在字符串中 in / not in

print('l' in str1)
print('l' not in str2)

# 常用查找方法
paragraph = '我是一名大三学生,重新对python语言进行巩固学习'
print(len(paragraph))  # 获取字符串长度
print(paragraph.startswith("我是"))  # 指定字符串开头
print(paragraph.endswith("学习"))  # 指定字符串结尾
print(paragraph.find("python"))  # 寻找第一次出现指定字符串的索引
print(paragraph.rfind("巩固"))  # 寻找最后一次指定字符串的索引
print(paragraph.count("语言"))  # 计算指定字符出现的次数
print(paragraph.isalnum())  # 判断字符串全部是否是字母或数字
print(paragraph.isdigit())  # 判断字符串全部是否是数字

# 去除首尾信息
paragraph = '我就是我'
print(paragraph.strip("我"))  # 去除首尾指定字符
print(paragraph.lstrip('我'))  # 去除左边指定字符
print(paragraph.rstrip('我'))  # 去除右边指定字符

# 大小写转换
a = 'my love a gril'
b = a.capitalize()  # 产生新的字符串,首字母大写
print(b)
b = a.title()  # 产生新的字符串,每个单词首字母大写
print(b)
b = a.upper()  # 产生新的字符串,每个字母转换成大写
print(b)
b = a.lower()  # 产生新的字符串,每个字母转换成小写
print(b)
b = a.swapcase()  # 产生新的字符串,每个字母大小写转换
print(b)
print(a)
