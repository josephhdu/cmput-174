# This program uses a grid of cells on a map, with each cell representing a value.
# However, there are empty cells represented by 0 and these empty cells are filled by averaging out its neighbors.

def create_grid(filename):
    # Reads a text file and uses a nested for loop to create a grid
    # - filename: string that represents the text file's name

    # Opens the file and reads contents
    filemode = 'r'
    file = open(filename,filemode)
    contents = file.readlines()
    file.close()
 
    # Gets the dimensions of the grid
    width = int(contents.pop(0))
    height = int(contents.pop(0))
    
    # Nested for loop that creates the grid
    grid = []
    for i in range(width):
        row = []
        for i in range(height):
            number = int(contents.pop(0))
            row.append(number)
        grid.append(row)
    return grid

def display_grid(grid):
    # For loop that displays the grid
    # - grid: list that contains the grid
    for row in grid:
        for i in row:
            print('|', i,end=' ')
        print('|')
    print('')

def find_neighbors(row_index, col_index, grid):
    # Checks the position of the cell and returns its neighbors
    # - row_index: int that represents the row index
    # - col_index: int that represents the column index
    # - grid: list that contains the grid

    # Assignments
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []

    # Checks if position is in the corner
    if row_index - 1 < 0 and col_index - 1 < 0:
        neighbors.append(grid[row_index][col_index + 1])
        neighbors.append(grid[row_index + 1][col_index])
        neighbors.append(grid[row_index + 1][col_index + 1])
        return neighbors
    elif row_index + 1 > rows - 1 and col_index - 1 < 0:
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index - 1][col_index + 1])
        neighbors.append(grid[row_index][col_index + 1])
        return neighbors
    elif row_index - 1 < 0 and col_index + 1 > cols - 1:
        neighbors.append(grid[row_index][col_index - 1])
        neighbors.append(grid[row_index + 1][col_index - 1])
        neighbors.append(grid[row_index + 1][col_index])
        return neighbors
    elif row_index + 1 > rows - 1 and col_index + 1 > cols - 1:
        neighbors.append(grid[row_index - 1][col_index - 1])
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index][col_index - 1])
        return neighbors
    # Checks if position is an edge
    elif row_index - 1 < 0:
        neighbors.append(grid[row_index][col_index - 1])
        neighbors.append(grid[row_index][col_index + 1])
        neighbors.append(grid[row_index + 1][col_index - 1])
        neighbors.append(grid[row_index + 1][col_index])
        neighbors.append(grid[row_index + 1][col_index + 1])
        return neighbors
    elif row_index + 1 > rows - 1: 
        neighbors.append(grid[row_index - 1][col_index - 1])
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index - 1][col_index + 1])
        neighbors.append(grid[row_index][col_index - 1])
        neighbors.append(grid[row_index][col_index + 1])
        return neighbors
    elif col_index - 1 < 0:
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index - 1][col_index + 1])
        neighbors.append(grid[row_index][col_index + 1])
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index - 1][col_index + 1])
        return neighbors
    elif col_index + 1 > cols - 1:
        neighbors.append(grid[row_index - 1][col_index - 1])
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index][col_index - 1])
        neighbors.append(grid[row_index - 1][col_index - 1])
        neighbors.append(grid[row_index - 1][col_index])
        return neighbors
    # Checks for any other position
    else:
        neighbors.append(grid[row_index - 1][col_index - 1])
        neighbors.append(grid[row_index - 1][col_index])
        neighbors.append(grid[row_index - 1][col_index + 1])
        neighbors.append(grid[row_index][col_index - 1])
        neighbors.append(grid[row_index][col_index + 1])
        neighbors.append(grid[row_index + 1][col_index - 1])
        neighbors.append(grid[row_index + 1][col_index])
        neighbors.append(grid[row_index + 1][col_index + 1])
        return neighbors

def fill_gaps(grid):
    # Fills the zeros in the grid
    # - grid: list that contains the grid

    # Checks the position of the zero
    zero_list = []
    for ri in range(len(grid)):
        for ci in range(len(grid)):
            if grid[ri][ci] == 0:
                zero_list.append([ri,ci])
    
    # Calulates what the zero should be and replaces it
    for i in range(len(zero_list)):
        row_index = zero_list[i][0]
        col_index = zero_list[i][1]
        values = (find_neighbors(row_index, col_index, grid))
        sum = 0
        for i in range(0, len(values)):
            sum = sum + values[i]
        zero_val = sum//len(values)
        for ri in range(len(grid)):
            for ci in range(len(grid)):
                grid[row_index][col_index] = zero_val

def find_max(grid):
    # Goes through the grid and finds the maximum value
    # - grid: list that contains the grid
    max = 0
    for ri in range(len(grid)):
        for ci in range(len(grid)):
            if grid[ri][ci] > max:
                max = grid[ri][ci]
    return max
    
def find_average(grid):
    # Goes through the grid and find the average value
    # - grid: list that contains the grid
    avg = 0 
    total = 0
    for ri in range(len(grid)):
        for ci in range(len(grid)):
            avg = avg + grid[ri][ci]
            total += 1
    avg = avg//total
    return avg

def main():
    # Main function
    file = 'grid.txt'
    grid = create_grid(file)
    print('This is our grid:')
    display_grid(grid)
    fill_gaps(grid)
    print('This is out newly calculated grid:')
    display_grid(grid)

    # Displays Stats
    print('Average housing price in this area is: ',find_average(grid))
    print('Maximum housing price in thie ares is: ', find_max(grid))
    
main()