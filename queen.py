def solve_n_queens(n, row=0, cols=set(), diag1=set(), diag2=set(), board=[]):
    if row == n:
        return [board]
    solutions = []
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        solutions += solve_n_queens(n, row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col}, board + [col])
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for row in sol:
            print("." * row + "Q" + "." * (n - row - 1))
        print()

n = 8  # Change N as needed
solutions = solve_n_queens(n)
print("Total solutions:", len(solutions))
print_solutions(solutions, n) 