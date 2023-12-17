

a=[[0,0,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9],[1,2,3,4,4,5,7,8,9]]

def get_block_num(p,q):
    return(a[p-1][q-1])


def get_inside_block(p,q):
    i=0
    while q-3*i>0:
        i=i+1
    q=i
    j=0
    while p-3*j>0:
        j=j+1
    q=i+((j-1)*3)
    p=p%3
    if p==0:
        p=3
    return(p,q)

def get_block(n):
    a=0
    b=0
    q=n%3
    if q==0:
        a=7
    elif q==1:
        a=1
    else:
        a=4
    i=0
    while (n-3*i)>0:
        i=i+1
    if i==1:
        b=1
    elif i==2:
        b=4
    else:
        b=7
    return(b,a)

def print_block(n):
    l=[]
    (x,y)=get_block(n)
    for i in range (x,x+3):
        for j in range (y,y+3):
            l.append(get_block_num(i,j))
    return(l)


def get_row(n):
    return(a[n-1])


def get_column(n):
    L=[]
    for i in range (0,9):
        L.append(a[i][n-1])
    return(L)


def check(i):
    for j in range(0,9):
        if a[i][j]==0:
            return(True)
    return(False)

def uassigned_position(a):
    i=0
    while i<9:
        i=i+1
        if check(i-1):
            break
    j=0
    while j<9:
        j=j+1
        if a[i-1][j-1]==0:
            break
    return(i,j)




def valid_list(l):
    for i in range (0,len(l)):
        for j in range (i+1,len(l)):
            if l[i]==l[j] or l[i]==0:
                return(False)
    if l[-1]!=0:
        return(True)
    else:
        return(False)





def valid_sudoku(a):
    for i in range (1,9):
        if valid_list(get_row(i))==False:
            return False
    for i in range (1,9):
        if valid_list(get_column(i))==False:
            return False
    for i in range (1,9):
        if valid_list(print_block(i))==False:
            return False
    return(True)





def get_candidates(p,q):
    l=[1,2,3,4,5,6,7,8,9]
    for i in get_row(p):
        for j in l:
            if i==j:
                l.remove(j)
    for i in get_column(q):
        for j in l:
            if i==j:
                l.remove(j)
    for i in print_block(get_inside_block(p,q))
        for j in l:
            if i==j:
                l.remove(j)
    return(l)


def make_move(a,p,q,n):
    a[p][q]=n
    return(a)


def undo_move(a,p,q):
    a[p][q]=0
    return(a)

def sudoku_solver(a):
    def is_valid_move(board, row, col, num):
        # Check if 'num' is not already present in the current row, column, or 3x3 block
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def find_empty_cell(board):
        # Find the first empty cell (cell with 0) in the Sudoku board
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def solve_sudoku(board):
        empty_cell = find_empty_cell(board)

        # If there are no empty cells, the Sudoku puzzle is solved
        if not empty_cell:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if is_valid_move(board, row, col, num):
                board[row][col] = num

                # Recursively attempt to solve the puzzle
                if solve_sudoku(board):
                    return True

                # If the current configuration doesn't lead to a solution, backtrack
                board[row][col] = 0

        return False

    if solve_sudoku(a):
        return a
    else:
        return None


