'''  apples Alice  dogs
    oranges   Bob  cats
   cherries Carol moose
     banana David goose           Вывести список в таком виде.'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(m):
    colWidths = [0]*len(tableData)
    for x in range (0, 3):
        for y in range (0,4):
            if colWidths[x]<len(tableData[x][y]):
                colWidths[x] = len(tableData[x][y])
    for q in range (0,4):
        for w in range(0,3):
            if w == (len(colWidths)-1):
                print(tableData[w][q].rjust(colWidths[w]))
            else:
                print(tableData[w][q].rjust(colWidths[w]), end=" ")

printTable(tableData)