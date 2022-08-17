def isValid(s: str) -> bool:

    stack = []  # store open parentheses
    for c in s:
        if (c == '(' or c == '[' or c == '{'):
            stack.append(c)
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c == '}' and stack and stack[-1] == '{':
            stack.pop()
        elif c == ']' and stack and stack[-1] == '[':
            stack.pop()
        else:
            return False
    
    return len(stack) == 0

isValid("()[]{}")