stuff = {'rope': 1, 'totch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonloot = ['gold coin','gold coin','gold coin','totch','arrow','arrow']
def displayInbentory(inv):
    print(inv)
    item_total = 0
    for k, v in inv.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number: ' + str(item_total))

def addInv(inv,ninv):
    item_total = 0
    for x in ninv:
        for k, v in inv.items():
            if k == x:
                inv[k] += 1
    for k, v in inv.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number: ' + str(item_total))

addInv(stuff, dragonloot)


