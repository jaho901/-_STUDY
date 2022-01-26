import sys
sys.stdin = open('1935.txt')

n = int(input())
data = list(input())
# 영문과 연산자를 구분할 수 있는 방법 => 대문자인지 아닌지
number = []
for _ in range(n):
    number.append(int(input()))
# print(number)
stack = []

for i in range(len(data)):
    if data[i].isupper():
        # 각각의 대문자는 숫자를 지정해둠
        stack.append(number[ord(data[i]) - ord('A')])
    else:
        last_number = stack.pop()
        first_number = stack.pop()
        if data[i] == "+":
            stack.append(first_number + last_number)
        elif data[i] == "-":
            stack.append(first_number - last_number)
        elif data[i] == "*":
            stack.append(first_number * last_number)
        elif data[i] == "/":
            stack.append(first_number / last_number)

print("{:.2f}".format(stack[0]))
