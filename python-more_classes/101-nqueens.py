#!/usr/bin/python3
"""
Solves the N-queens puzzle by placing N non-attacking queens on an NxN board.
"""
import sys


def solve_nqueens():
    """
    Main function to handle input validation and initiate the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # board will store the column index for each row: board[row] = col
    board = []
    backtrack(n, 0, board)


def is_safe(board, row, col):
    """
    Checks if placing a queen at (row, col) is safe from other queens.
    """
    for r, c in enumerate(board):
        # Check column conflict and diagonal conflicts
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def backtrack(n, row, board):
    """
    Uses recursion to find all possible placements of queens.
    """
    if row == n:
        # Format the result as [[row, col], [row, col], ...]
        result = [[r, c] for r, c in enumerate(board)]
        print(result)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            backtrack(n, row + 1, board)
            board.pop()  # Backtrack


if __name__ == "__main__":
    solve_nqueens()
