# Comma Code
import copy

def comma_code(list_value):
  local = copy.copy(list_value)
  result = ''

  for i in range(len(local)):
    if i != len(local) - 1:
      result += (f'{str(local[i])}, ')
    else:
      result += (f'and {str(local[i])}')
  
  return result


spam = ['apples', 'bananas', True, 'cats', 14]
# print(comma_code(spam))





# Character Picture Grid
grid = [
  ['.', '.', '.', '.', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['.', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'O', '.'],
  ['O', 'O', 'O', 'O', '.', '.'],
  ['.', 'O', 'O', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.']
]

def render(grid):
  local_grid = copy.deepcopy(grid)

  for y in range(len(local_grid[0])):

    for x in range(len(local_grid)):

      if x != len(local_grid) - 1:
        print(f'{local_grid[x][y]}', end='')
      else:
        print(f'{local_grid[x][y]}')


# render(grid)