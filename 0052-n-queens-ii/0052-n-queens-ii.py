class Solution:
    def totalNQueens(self, n):
        count = [0]

        cols = set()
        positive_diagonal = set()
        negative_diagonal = set()

        def backtrack(row):
            if row == n:
                count[0] += 1
                return

            for col in range(n):
                if col in cols:
                    continue

                if row + col in positive_diagonal:
                    continue

                if row - col in negative_diagonal:
                    continue

                cols.add(col)
                positive_diagonal.add(row + col)
                negative_diagonal.add(row - col)

                backtrack(row + 1)

                cols.remove(col)
                positive_diagonal.remove(row + col)
                negative_diagonal.remove(row - col)

        backtrack(0)

        return count[0]