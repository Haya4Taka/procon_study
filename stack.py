inp = list(input().split(' '))
stack = []

for o in inp:
    if o in ["+", "-", "*"]:
        if o is "+":
            r = stack.pop() + stack.pop()
            stack.append(r)
        if o is "-":
            x = stack.pop()
            y = stack.pop()
            r = y - x
            stack.append(r)
        if o is '*':
            r = stack.pop() * stack.pop()
            stack.append(r)
    else:
        stack.append(int(o))

print(stack.pop())