class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    bit = 1 << (int(board[r][c]) - 1)
                    box = (r // 3) * 3 + (c // 3)

                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[box] |= bit

        def backtrack(index):
            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row // 3) * 3 + (col // 3)

            used = rows[row] | cols[col] | boxes[box]

            for num in range(1, 10):
                bit = 1 << (num - 1)

                if used & bit:
                    continue

                board[row][col] = str(num)

                rows[row] |= bit
                cols[col] |= bit
                boxes[box] |= bit

                if backtrack(index + 1):
                    return True

                rows[row] ^= bit
                cols[col] ^= bit
                boxes[box] ^= bit
                board[row][col] = "."

            return False

        backtrack(0)