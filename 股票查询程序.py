f = open(file='股票数据源.txt', mode='r', encoding='utf-8')
lines_data = []
for line in f:
    line_data = line.split(',')
    lines_data.append(line_data)
lines_data[0].insert(0, '序列')
for i in range(1, 91):
    lines_data[i].insert(0, str(i))


def sort_share(datas_number):
    if len(datas_number[10]) == 2:
        num = (((15 - len(datas_number[10])) - 1) * ' ')
    else:
        num = ((15 - len(datas[10])) * ' ')
    print(datas_number[0] + ((8 - len(datas_number[0])) * ' ') + datas_number[1] + '	' + datas_number[2] + '		' +
          datas_number[3] + '		' + datas_number[4] + '		' + datas_number[5] + '		' + datas_number[6] +
          ((11 - len(datas_number[6])) * ' ') + datas_number[7] + ((13 - len(datas_number[7])) * ' ') + datas_number[8]
          + ((11 - len(datas_number[8])) * ' ') + datas_number[9] + ((13 - len(datas_number[9])) * ' ')
          + datas_number[10] + num + datas_number[11] + ((12 - len(datas_number[11])) * ' ') + datas_number[12], end='')


key = True
while key:
    select = input("请输入查询关键字:")
    print(lines_data[0][0] + '\t\t' + lines_data[0][1] + '\t\t' + lines_data[0][2] + '\t\t' +
          lines_data[0][3] + '\t\t' + lines_data[0][4] + '\t\t' + lines_data[0][5] + '\t\t' +
          lines_data[0][6] + '\t\t' + lines_data[0][7] + '\t\t' + lines_data[0][8] + '\t\t' +
          lines_data[0][9] + '\t\t' + lines_data[0][10] + '\t\t' + lines_data[0][11] + '\t\t' +
          lines_data[0][12], end='')
    count = 0
    for datas in lines_data[1:]:
        if select == datas[0]:
            count += 1
            sort_share(datas)
        elif select[0:3] == lines_data[0][3]:
            if select[3:4] == '>':
                if float(datas[3]) > float(select[4:]):
                    count += 1
                    sort_share(datas)
            elif select[3:4] == '<':
                if float(datas[3]) < float(select[4:]):
                    count += 1
                    sort_share(datas)
            else:
                count += 1
                sort_share(datas)
        elif select[0:] in datas[2]:
            count += 1
            sort_share(datas)
        elif select[0:3] == lines_data[0][5]:
            if select[3:4] == '>':
                if float(datas[5][1:-1]) > float(select[4:]):
                    count += 1
                    sort_share(datas)
            elif select[3:4] == '<':
                if float(datas[5][1:-1]) < float(select[4:]):
                    count += 1
                    sort_share(datas)
            else:
                count += 1
                sort_share(datas)
        elif select[0:3] == lines_data[0][9]:
            if select[3:4] == '>':
                if float(datas[9][1:-1]) > float(select[4:]):
                    count += 1
                    sort_share(datas)
            elif select[3:4] == '<':
                if float(datas[9][1:-1]) < float(select[4:]):
                    count += 1
                    sort_share(datas)
            else:
                count += 1
                sort_share(datas)
        elif select[0:3] in lines_data[0][10]:
            if select[3:] == datas[10][0:3]:
                count += 1
                sort_share(datas)
            elif select[3:4] == '>':
                if datas[10] != '亏损':
                    if float(datas[10]) > float(select[4:]):
                        count += 1
                        sort_share(datas)
            elif select[3:4] == '<':
                if datas[10] != '亏损':
                    if float(datas[10]) < float(select[4:]):
                        count += 1
                        sort_share(datas)
            elif select == "市盈率":
                count += 1
                sort_share(datas)
            else:
                pass
    print('\n', "共%d条记录" % count, sep='')
    key = input("是否退出(Y/N)").upper()
    if key == 'Y':
        break
