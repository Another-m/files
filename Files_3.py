def open_file(file_name):
    with open(file_name, encoding='utf-8') as file:
        list_strings = []
        for n, string in enumerate(file):
            count_str = n+1
            list_strings.append(string.strip())
        return [file.name, str(count_str)] + list_strings

def write_file(file_merge):
    with open('merge.txt', 'wt') as file:
        quant_str = dict()
        for n, line in enumerate(file_merge):
            quant_str[line[1]] = n
        quant_str_sort = sorted(quant_str.items())
        for element in quant_str_sort:
            for string in file_merge[element[1]]:
                file.write(string + '\n')


file_merge = [open_file('1.txt'), open_file('2.txt'), open_file('3.txt')]
print(file_merge)

write_file(file_merge)

