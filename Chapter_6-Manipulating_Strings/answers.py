#! python

'''
a program that displays a list of lists in a well formatted tabular structure
'''

tableData = [
  ['apples', 'oranges', 'cherries', 'banana'],
  ['Alice', 'Bob', 'Carol', 'David'],
  ['dogs', 'cats', 'moose', 'goose']
]


def printTable(entries: list) -> None:
  colWidths = [0] * len(entries)

  # loop to determing the justification(padding) length
  for rowIndex in range(len(entries)):
    for word in entries[rowIndex]:
      if len(word) > colWidths[rowIndex]:
        colWidths[rowIndex] = len(word)
  
  # loop to render the entries in a tabular form
  for j in range(len(entries[0])):
    line = ''
    for i in range(len(entries)):
      line += (f'{entries[i][j].rjust(colWidths[i])} ')
      if i == len(entries) - 1:
        print(line)




printTable(tableData)