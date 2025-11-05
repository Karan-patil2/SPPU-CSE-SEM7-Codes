def n_queens(n):
    res, board = [], [["0"] * n for _ in range(n)]
    cols, pos, neg = set(), set(), set()

    def backtrack(r):
        if r == n:
            res.append([" ".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r + c) in pos or (r - c) in neg:
                continue
            cols.add(c); pos.add(r + c); neg.add(r - c); board[r][c] = "1"
            backtrack(r + 1)
            cols.remove(c); pos.remove(r + c); neg.remove(r - c); board[r][c] = "0"

    backtrack(0)
    for sol in res:
        print("\n".join(sol), "\n")

if __name__ == "__main__":
    n_queens(8)
