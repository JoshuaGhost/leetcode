class Solution:
    def operate(self, a, b, op):
        if op == '*':
            return a * b
        if op == '+':
            return a + b
        if op == '/':
            return a // b
        return a-b
    
    def calculate(self, s: str) -> int:
        s = s.strip()
        read_digit = False
        op_stack = []
        dig_stack = []
        for c in s:
            if c.isspace():
                continue
                
            if c.isdigit():
                if not read_digit:
                    read_digit = True
                    pivot_num = 0
                pivot_num = pivot_num * 10 + int(c)
                continue
                
            dig_stack.append(pivot_num)
            read_digit = False    
                
            if not op_stack:
                pass
            elif c in '-+':
                while op_stack:
                    b = dig_stack.pop()
                    a = dig_stack.pop()
                    op = op_stack.pop()
                    dig_stack.append(self.operate(a, b, op))
            else:
                while op_stack and op_stack[-1] not in '+-':
                    b = dig_stack.pop()
                    a = dig_stack.pop()
                    op = op_stack.pop()
                    dig_stack.append(self.operate(a, b, op))
            op_stack.append(c)
        dig_stack.append(pivot_num)
        while op_stack:
            b = dig_stack.pop()
            a = dig_stack.pop()
            op = op_stack.pop()
            dig_stack.append(self.operate(a, b, op))
        return dig_stack[0]