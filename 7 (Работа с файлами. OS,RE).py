'''Создайте программу Mad Libs, которая читает текстовые файлы и позволяет пользователю добавлять свой
   собственный текст везде, где в текстовом файле появляется слово ADJECTIVE, NOUN, ADVERB или VERB.'''

import os, re
pfr = open('C:\\Games\\2.txt','r').read()
print(pfr)
pfr = pfr.replace("ADJECTIVE", input('Введите прилогательное:  ')).replace("NOUN", input('Введите существительное:  ')).replace("VERB", input('Введите глагол:  '))
print(pfr)
pfrn = open('C:\\Games\\2.txt','w')
pfrn.write(pfr)

'''Напишите программу, которая открывает все TXT-файлы в папке и ищет любую строку, 
   соответствующую введенному пользователем регулярному выражению. 
   Результаты должны быть выведены на экран. '''

print('\n************************-------**************************************')
t = os.listdir("C:\\Games\\123\\")                              # Вывод в переменную t списка файлов директории
tn = []
for x in range (len(t)-1):
    if t[x].endswith('.txt'):                                   # Сортировка файлов, чтобы остались только текстовые файлики
        tn.append(t[x])
for y in range (len(tn)):
    f = open('C:\\Games\\123\\' + str(tn[y]), 'r').read()
    s = re.compile(r'[\w.-|\s]+[\d\d\d]+[\w.-|\s]+')
    mo = s.findall(f)
    print(mo)



