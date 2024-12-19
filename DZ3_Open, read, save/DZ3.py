dict_ = {}
with open('1.txt', encoding='utf-8') as f:
    count_1 = 0
    name_1 = '1.txt'
    lines_1 = ""
    for line in f:
        count_1 += 1
        lines_1 += line
    text_1 = name_1 + '\n' + str(count_1) + '\n' + lines_1 + '\n'
    dict_[count_1] = text_1

with open('2.txt', encoding='utf-8') as f:
    count_2 = 0
    name_2 = '2.txt'
    lines_2 = ""
    for line in f:
        count_2 += 1
        lines_2 += line
    text_2 = name_2 + '\n' + str(count_2) + '\n' + lines_2 + '\n'
    dict_[count_2] = text_2

with open('3.txt', encoding='utf-8') as f:
    count_3 = 0
    name_3 = '3.txt'
    lines_3 = ""
    for line in f:
        count_3 += 1
        lines_3 += line
    text_3 = name_3 + '\n' + str(count_3) + '\n' + lines_3 + '\n'
    dict_[count_3] = text_3

with open('4.txt', 'w', encoding='utf-8') as f:
    for key in sorted(dict_.keys()):
        f.write(dict_[key])