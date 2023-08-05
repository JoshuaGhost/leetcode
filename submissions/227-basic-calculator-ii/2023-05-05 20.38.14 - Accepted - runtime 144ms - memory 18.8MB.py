class Solution:
    def operate(self, a, b, op):
        if op == '*':
            return a * b
        if op == '+':
            return a + b
        if op == '/':
            return a // b if a*b >= 0 else -(abs(a) // abs(b))
        return a-b
    
    def calculate(self, s: str) -> int:
        s = s.strip()
        read_digit = False
        op = '+'
        prev_num = 0
        temp_res = 0
        for c in s:
            if c.isspace():
                continue
                
            if c.isdigit():
                if not read_digit:
                    read_digit = True
                    pivot_num = 0
                pivot_num = pivot_num * 10 + int(c)
                continue

            read_digit = False
                
            if op in '+-':
                temp_res += prev_num
                prev_num = -pivot_num if op == '-' else pivot_num
            else:
                prev_num = self.operate(prev_num, pivot_num, op)
            op = c
            
        if op in '+-':
            temp_res += prev_num
            prev_num = -pivot_num if op == '-' else pivot_num
        else:
            prev_num = self.operate(prev_num, pivot_num, op)

        temp_res += prev_num
        return temp_res