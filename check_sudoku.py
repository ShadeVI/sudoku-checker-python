PATTERN_ROW = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example valid grid
SUDOKU_GRID = [
    ["295743861"],
    ["431865927"],
    ["876192543"],
    ["387459216"],
    ["612387495"],
    ["549216738"],
    ["763524189"],
    ["928671354"],
    ["154938672"]
]

# Example no valid grid
NO_VALID_GRID = [
    ["195743862"],
    ["431865927"],
    ["876192543"],
    ["387459216"],
    ["612387495"],
    ["549216738"],
    ["763524189"],
    ["928671354"],
    ["254938671"]
]

# Welcome message function


def welcome_message():
    print("""
    ###############################################
    ###############################################
    #####                                     #####
    #####     S U D O K U   C H E C K E R     #####
    #####         ( ONLY 9 x 9 GRID)          #####
    #####                                     #####
    ###############################################
    ###############################################
    """)
# Convert string to cells of int


def convert_grid_type_cells(grid):
    new_grid = []
    for row in grid:
        for num_list_ch in row:
            new_row = [int(ch) for ch in num_list_ch]
            new_grid.append(new_row)
    return new_grid

# CHECK PATTERN


def check_rows(grid):
    for row in grid:
        sort_row = sorted(row)
        if sort_row != PATTERN_ROW:
            return False
    return True

# check COLUMNS converting to rows and using same check_rows function


def check_columns(grid):
    col_arr = []
    for cell in range(9):
        col = []
        for row in grid:
            col.append(row[cell])
        col_arr.append(col)
    return check_rows(col_arr)


def get_subsquare_3by3(grid, x, y):
    sub_square = []
    for i in range(x, x+3):
        for k in range(y, y+3):
            sub_square.append(grid[i][k])
    return sub_square

##### START PROGRAM ####


def run_prog():
    while True:
        try:
            user_grid = []
            # Get rows from user
            welcome_message()
            for i in range(9):
                while True:
                    row = input(
                        "Inserte la linea n. {} [type Q to exit]: ".format(i+1))
                    if row.upper() == "Q":
                        print("\n\nClosing the program! Bye!")
                        return False
                    elif row.isspace():
                        print("\nRow is not valid (Full of empty spaces)\n")
                    elif row == "":
                        print("\nRow is not valid (Empty)\n")
                    elif len(row.replace(" ", "")) < 9:
                        print("\nRow is not valid (lenght is not 9)\n")
                    elif not row.isnumeric():
                        print("\nRow is not valid (Contains not valid value)\n")
                user_grid.append([row])

            user_grid_converted = convert_grid_type_cells(user_grid)

            # LOOP THROUGH GRID AND GET SUBGRID_3BY3 AND PUT IN A LIST
            grid_of_rows_repr_subsquares = []
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    grid_of_rows_repr_subsquares.append(
                        get_subsquare_3by3(user_grid_converted, i, j))

            # CHECK SUBGRIDS
            if check_rows(user_grid_converted) and check_columns(user_grid_converted) and check_rows(grid_of_rows_repr_subsquares):
                print("Yes")
            else:
                print("No")
        except:
            print("\n\nOps, something bad happened... Restart the program...")
            exit()


run_prog()
