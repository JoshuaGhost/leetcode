from typing import List


class Solution:
    def rectify_line(self, line: List[str]) -> str:
        if len(line) == 1:
            return line[0] + " " * (self.max_width - len(line[0]))
        chars_length = sum(map(len, line))
        num_space = self.max_width - chars_length
        base_num_space = num_space // (len(line) - 1)
        num_space_modulo = num_space % (len(line) - 1)
        ret = ""
        for i, word in enumerate(line[:-1]):
            ret += word + base_num_space * " "
            if i < num_space_modulo:
                ret += " "
        ret += line[-1]
        return ret

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        self.max_width = maxWidth
        line = []
        ret = []
        line_length = 0
        for word in words:
            if not line:
                line.append(word)
                line_length = len(word)
            elif line_length + 1 + len(word) > maxWidth:
                ret.append(self.rectify_line(line))
                line = [word]
                line_length = len(word)
            else:
                line_length += 1 + len(word)
                line.append(word)
        if line:
            last_line_content = " ".join(line)
            ret.append(last_line_content + " " * (maxWidth - len(last_line_content)))
        return ret


