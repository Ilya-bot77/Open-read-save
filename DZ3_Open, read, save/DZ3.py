import os
file_list = os.listdir(r"Original text") # Исходные файлы *.txt должны быть в данной папке
dict_text = {}
# print(file_list)

def transformation(self):
    for name in self:
        file = f'Original text/{name}'
        # print(file)
        with open(file, encoding='utf-8') as f:
            count = 0
            lines = ""
            for line in f:
                count += 1
                lines += line
            text = name + '\n' + str(count) + '\n' + lines + '\n'
            dict_text[count] = text

transformation(file_list)

with open('Result.txt', 'w', encoding='utf-8') as f:
    for key in sorted(dict_text.keys()):
        f.write(dict_text[key])