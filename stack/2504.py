import sys
sys.stdin = open('2504.txt')

data = list(input())
# print(data)
stack = []
result = 0
sub = 1

for i in range(len(data)):
    if data[i] == "(":
        stack.append(data[i])
        sub *= 2

    elif data[i] == "[":
        stack.append(data[i])
        sub *= 3

    elif data[i] == ")":
        if len(stack) == 0 or stack[-1] == "[":
            result = 0
            break
        elif data[i-1] == "(":
            result += sub
#       그 외의 경우는 ')' or ']'가 나오는 경우
        stack.pop()
        sub //= 2

    elif data[i] == "]":
        if len(stack) == 0 or stack[-1] == "(":
            result = 0
            break
        elif data[i-1] == "[":
            result += sub
        stack.pop()
        sub //= 3

if stack:
    print(0)
else:
    print(result)




