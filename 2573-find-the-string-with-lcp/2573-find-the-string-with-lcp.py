class Solution(object):
    def findTheString(self, lcp):
        n = len(lcp)

        # Check diagonal
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # parent[i] tells which group position i belongs to
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a != b:
                parent[b] = a

        # If lcp[i][j] > 0, word[i] and word[j]
        # must contain the same first character.
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)

        # Assign smallest possible characters
        group_char = {}
        next_char = ord('a')
        word = [''] * n

        for i in range(n):
            root = find(i)

            if root not in group_char:
                if next_char > ord('z'):
                    return ""

                group_char[root] = chr(next_char)
                next_char += 1

            word[i] = group_char[root]

        # Verify the entire LCP matrix
        for i in range(n):
            for j in range(n):

                if word[i] != word[j]:
                    if lcp[i][j] != 0:
                        return ""

                else:
                    expected = 1

                    if i + 1 < n and j + 1 < n:
                        expected += lcp[i + 1][j + 1]

                    if lcp[i][j] != expected:
                        return ""

        return ''.join(word)