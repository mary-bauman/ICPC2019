def checkSameColumn(grid):
    #Check for same num of whites and blacks in row
    for i in range(len(grid[0])):
        white = 0
        for j in range(len(grid)):
            if grid[j][i] == 'W':
                white += 1
        if white != len(grid) - white:
            return False
    return True

def checkSameRows(grid):
    #Check for same num of whites and blacks in row
    for i in range(len(grid)):
        white = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 'W':
                white += 1
        if white != len(grid[i]) - white:
            return False
    return True

def checkConsecutiveRows(grid):
#Check for consecutive row
    for i in range(len(grid)):
        consecutive = 0
        for j in range(len(grid[i]) - 1):
            if grid[i][j] == grid[i][j + 1]:
                consecutive += 1
            else:
                consecutive = 0
            if consecutive > 1:
                return False
    return True

def checkConsecutiveColumns(grid):
#Check for consecutive row
    for i in range(len(grid[0])):
        consecutive = 0
        for j in range(len(grid) - 1):
            if grid[j][i] == grid[j + 1][i]:
                consecutive += 1
            else:
                consecutive = 0
            if consecutive > 1:
                return False
    return True

grid = []
with open("C.txt") as f:
    testCase = int(f.readline())

    for i in range(testCase):
        line = f.readline().strip()
        
        row = []
        for i in range(len(line)):
            row.append(line[i])
        grid.append(row)


print(checkSameColumn(grid) and checkSameColumn(grid) and checkConsecutiveRows(grid)
      and checkConsecutiveColumns(grid))