class Solution:
    def solveNQueens(self, n):
        result = []

        board = [["."] * n for _ in range(n)]

        cols = set()
        positive_diagonal = set()
        negative_diagonal = set()

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols:
                    continue

                if row + col in positive_diagonal:
                    continue

                if row - col in negative_diagonal:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                positive_diagonal.add(row + col)
                negative_diagonal.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                cols.remove(col)
                positive_diagonal.remove(row + col)
                negative_diagonal.remove(row - col)

        backtrack(0)

        return result