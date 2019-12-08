import re
def Proverka (pass1):
    x = re.compile(r'[A-Z]')
    mo1 = x.findall(pass1)
    y = re.compile(r'[a-z]')
    mo2 = y.findall(pass1)
    z = re.compile(r'[0-9]')
    mo3 = z.findall(pass1)
    if len(pass1) != 8 or mo1 == [] or mo2 == [] or mo3 == []:
        return ('Пароль не удовлетворяет условиям!!')
    else:
        return ('Пароль принят')
p = ''
while p != 'Пароль принят':
    p = Proverka(input('Введите пароль:  '))
    print(p)


