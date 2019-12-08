import re

def fremove (slovo, simvol=''):
    if simvol != '':
        ew2 = re.compile(simvol)
        mo2 = ew2.sub(r'', slovo)
        return (mo2)
    else:
        ew = re.compile(r'^\s')
        mo = ew.sub(r'', slovo)
        ew1 = re.compile(r'\s$')
        mo1 = ew1.sub(r'', mo)
        return (mo1)

print(fremove(' volk ','l'))