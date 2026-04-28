class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        key = tokens.pop()
        if key == '+':
            return self.evalRPN(tokens) + self.evalRPN(tokens)
        elif key == '-':
            return -1*self.evalRPN(tokens) + self.evalRPN(tokens)
        elif key == '*':
            return self.evalRPN(tokens) * self.evalRPN(tokens)
        elif key == '/':
            return int((1 / self.evalRPN(tokens)) * self.evalRPN(tokens))
        else:
            return int(key)