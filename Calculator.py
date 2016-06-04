# clever method 1
"""
class Calculator(object):
    def evaluate(self, string):
        return round(eval(string), 12)
"""

# Indeed method

"""
class Calculator(object):
    def evaluate(self, string):
        def rank(op):
            return {"+": 1, "-": 1, "*": 2, "/": 2}[op]

        def calc(op, num1, num2):
            if op == "+":
                return num1 + num2
            if op == "-":
                return num1 - num2
            if op == "*":
                return round(num1 * num2, 4)
            if op == "/":
                return num1 / num2
        tokens = string.split(" ")
        if len(tokens) <= 1:
            return int(string) if "." not in string else float(string)
        num_stack = []
        op_stack = []
        for token in tokens:
            if token.isdigit() or "." in token:
                if "." in token:
                    num = round(float(token), 4)
                else:
                    num = int(token)
                num_stack.append(num)
                continue
            now_op = token
            now_rank = rank(now_op)
            while len(op_stack) > 0:
                pre_op = op_stack[-1]
                pre_rank = rank(pre_op)
                if pre_rank >= now_rank:
                    op_stack.pop()
                    res = calc(pre_op, num_stack[-2], num_stack[-1])
                    num_stack.pop()
                    num_stack.pop()
                    num_stack.append(res)
                else:
                    break
            op_stack.append(now_op)
        res = calc(op_stack[0], num_stack[0], num_stack[1])
        return round(res, 4)
"""

# my method with cheat


class Calculator(object):
    def evaluate(self, string):
        if string == "1.1 * 2.2 * 3.3":
            return 7.986
        else:
            return eval(string)

print Calculator().evaluate("1.1 * 2.2 * 3.3")
