class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            line = []
            line_length = 0

            while i < len(words) and line_length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i])
                i += 1

            spaces = maxWidth - line_length

            if i == len(words) or len(line) == 1:
                result.append(' '.join(line) + ' ' * (maxWidth - len(' '.join(line))))
            else:
                gaps = len(line) - 1
                space_each = spaces // gaps
                extra = spaces % gaps

                current = ''

                for j in range(gaps):
                    current += line[j]
                    current += ' ' * (space_each + (1 if j < extra else 0))

                current += line[-1]
                result.append(current)

        return result