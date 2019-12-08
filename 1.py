def stroka(x):
    y=''
    for z in x:
        if z == x[0]:
            y = y + z
        elif z == x[len(x)-1]:
            y = y + ', and ' + z
        else:
            y = y + ', ' + z
    return(y)

spam = ['apples', 'bananas', 'tofu', 'cats', "dog"]
print(stroka(spam))