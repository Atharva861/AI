def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    # Check left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    # Check right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        print_board(board)
        return True  # Stop recursion once a solution is found
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True  # Place the queen
            if solve_n_queens_backtracking(board, row + 1, n):  # If a
                return True  # solution is found, stop
            board[row][col] = False  # Backtrack
    return False  # No solution found at this branch

def n_queens_backtracking(n):
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens_backtracking(board, 0, n):
        print("No solution exists.")

def is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
    return not (cols[col] or diags1[row + col] or diags2[row - col + (n - 1)])

def solve_n_queens_branch_and_bound(row, n, cols, diags1, diags2, board):
    if row == n:
        print_board(board)
        return True  # Stop recursion once a solution is found
    for col in range(n):
        if is_safe_branch_and_bound(row, col, cols, diags1, diags2, n):
            board[row][col] = True
            cols[col] = True
            diags1[row + col] = True
            diags2[row - col + (n - 1)] = True

            if solve_n_queens_branch_and_bound(row + 1, n, cols, diags1, diags2, board):
                return True  # If a solution is found, stop
            
            board[row][col] = False
            cols[col] = False
            diags1[row + col] = False
            diags2[row - col + (n - 1)] = False
    return False  # No solution found at this branch

def n_queens_branch_and_bound(n):
    board = [[False] * n for _ in range(n)]
    cols = [False] * n
    diags1 = [False] * (2 * n - 1)
    diags2 = [False] * (2 * n - 1)

    if not solve_n_queens_branch_and_bound(0, n, cols, diags1, diags2, board):
        print("No solution exists.")

# Run the solutions
if __name__ == "__main__":
    n = 8  # Change this value to test different board sizes
    print("Backtracking Solution:")
    n_queens_backtracking(n)
    print("\nBranch and Bound Solution:")
    n_queens_branch_and_bound(n)