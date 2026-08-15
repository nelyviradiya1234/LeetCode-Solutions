class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        s = list(s)

        # Each node:
        # [first_char, last_char, prefix, suffix, best, length]
        tree = [None] * (4 * n)

        def merge(left, right):
            first_char = left[0]
            last_char = right[1]

            length = left[5] + right[5]
            prefix = left[2]
            suffix = right[3]
            best = max(left[4], right[4])

            if left[1] == right[0]:
                best = max(best, left[3] + right[2])

                if left[2] == left[5]:
                    prefix = left[5] + right[2]

                if right[3] == right[5]:
                    suffix = left[3] + right[5]

            return [
                first_char,
                last_char,
                prefix,
                suffix,
                best,
                length
            ]

        def build(node, start, end):
            if start == end:
                tree[node] = [
                    s[start],
                    s[start],
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (start + end) // 2

            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, start, end, index, char):
            if start == end:
                tree[node] = [
                    char,
                    char,
                    1,
                    1,
                    1,
                    1
                ]
                return

            mid = (start + end) // 2

            if index <= mid:
                update(node * 2, start, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, end, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for i in range(len(queryIndices)):
            index = queryIndices[i]
            char = queryCharacters[i]

            update(1, 0, n - 1, index, char)

            answer.append(tree[1][4])

        return answer