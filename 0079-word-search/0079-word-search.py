class Solution:
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True

            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            if board[row][col] != word[index]:
                return False

            temp = board[row][col]
            board[row][col] = "#"

            found = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
            )

            board[row][col] = temp

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False