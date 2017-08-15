def isValid(s):
    BRACKETS_MAP = {"[": "]", "{": "}", "(": ")"}
    stack = []
    for bracket in s:
        if bracket in BRACKETS_MAP:
            stack.append(BRACKETS_MAP[bracket])
        elif not stack or bracket != stack.pop():
            return False
    return not stack

print(isValid('{[}]'))