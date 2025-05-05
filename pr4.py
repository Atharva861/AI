def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

# ---------- Backtracking ----------

def is_safe_bt(board, row, col, n):
    for i in range(row):
        if board[i][col] or \
           (col - row + i >= 0 and board[i][col - row + i]) or \
           (col + row - i < n and board[i][col + row - i]):
            return False
    return True

def solve_bt(board, row, n):
    if row == n:
        print_board(board)
        return True
    for col in range(n):
        if is_safe_bt(board, row, col, n):
            board[row][col] = True
            if solve_bt(board, row + 1, n):
                return True
            board[row][col] = False
    return False

def n_queens_backtracking(n):
    board = [[False] * n for _ in range(n)]
    if not solve_bt(board, 0, n):
        print("No solution exists.")

# ---------- Branch and Bound ----------

def solve_bb(row, n, board, cols, diag1, diag2):
    if row == n:
        print_board(board)
        return True
    for col in range(n):
        d1 = row + col
        d2 = row - col + n - 1
        if not (cols[col] or diag1[d1] or diag2[d2]):
            board[row][col] = True
            cols[col] = diag1[d1] = diag2[d2] = True
            if solve_bb(row + 1, n, board, cols, diag1, diag2):
                return True
            board[row][col] = False
            cols[col] = diag1[d1] = diag2[d2] = False
    return False

def n_queens_branch_and_bound(n):
    board = [[False] * n for _ in range(n)]
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)  # row + col
    diag2 = [False] * (2 * n - 1)  # row - col + n - 1
    if not solve_bb(0, n, board, cols, diag1, diag2):
        print("No solution exists.")

# ---------- Run Both Methods ----------

if __name__ == "__main__":
    n = 8
    print("Backtracking Solution:")
    n_queens_backtracking(n)
    print("\nBranch and Bound Solution:")
    n_queens_branch_and_bound(n)
