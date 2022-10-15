# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Decoding text
with open('start_text.txt', 'r') as data:
    text = data.read()
print(f'Start text: {text}')
def text_coding(t):
    str_code = ''
    count = 1
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            count += 1
        else:
            str_code += str(count) + t[i]
            count = 1
    if count > 1 or (t[len(t) - 2]) != t[-1]:
        str_code += str(count) + t[-1]
    with open('encoded_text.txt', 'w') as data:
        data.write(str_code)
    return str_code
str_code = text_coding(text)
print(f'Decoded text: {str_code}')

# Uncoding text

with open('encoded_text.txt', 'r') as data:
    str_code = data.read()
print(f'Decoded text: {str_code}')

def text_decoding(t):
    number = ''
    str_text = ''
    for i in range(len(t)):
        if not t[i].isalpha():
            number += t[i]
        else:
            str_text += t[i] * int(number)
            number = ''

    with open('start_text.txt', 'w') as data:
        data.write(str_text)
    return str_text
str_text = text_decoding(str_code)
print(f'Uncoded text: {str_text}')