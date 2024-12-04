file = open('4.in')


global_word = 'XMAS'
grid = [[c for c in line] for line in file.readlines()]
def dfs(dir, i, j, word):
    if word == global_word:
        return 1
    
    if i >= len(grid) or i < 0 or j >= len(grid[i]) or j < 0:
        return 0

    c = grid[i][j]
    if word + c in global_word:
        word += c
        if dir == 'n':
            return dfs(dir, i+1, j, word)
        if dir == 'e':
            return dfs(dir, i-1, j, word)
        if dir == 's':
            return dfs(dir, i, j+1, word)
        if dir == 'w':
            return dfs(dir, i, j-1, word)
        if dir == 'ne':
            return dfs(dir, i+1, j+1, word)
        if dir == 'nw':
            return dfs(dir, i+1, j-1, word)
        if dir == 'se':
            return dfs(dir, i-1, j+1, word)
        if dir == 'sw':
            return dfs(dir, i-1, j-1, word)
    return 0

count = 0
for i,_ in enumerate(grid):
    for j,_ in enumerate(grid[i]):
        if grid[i][j] == 'X':
            count += dfs('n', i,j,'')
            count += dfs('e', i,j,'')
            count += dfs('s', i,j,'')
            count += dfs('w', i,j,'')
            count += dfs('nw', i,j,'')
            count += dfs('ne', i,j,'')
            count += dfs('sw', i,j,'')
            count += dfs('se', i,j,'')
print(count)

count = 0
for i,_ in enumerate(grid):
    for j,_ in enumerate(grid[i]):
        if grid[i][j] == 'A':
            global_word = 'MAS'
            attempt = 0
            attempt += dfs('ne', i-1,j-1,'')
            attempt += dfs('nw', i-1,j+1,'')
            attempt += dfs('se', i+1,j-1,'')
            attempt += dfs('sw', i+1,j+1,'')
            if attempt >= 2:
                count += 1 
print(count)
