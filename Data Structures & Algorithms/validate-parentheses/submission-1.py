class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {}
        lookup['('] = ')'
        lookup['{'] = '}'
        lookup['['] = ']'
        for c in s:
            if c in lookup:
                stack.append(lookup[c])
            else:
                if len(stack) == 0 or c != stack.pop():
                    return False

        return len(stack) == 0