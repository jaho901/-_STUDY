n = 437674
k = 3
'''

'''
# n = 110011
# k = 10

def solution(n, k):
    numbers_list = []
    while True:
        numbers_list.insert(0, n%k)
        n = n//k
        if n <= 0:
            break

    numbers = []
    sub = ''
    for i in numbers_list:
        if i != 0:
            sub += str(i)
        else:
            if sub:
                numbers.append(int(sub))
                sub = ''
            else:
                pass
    if sub:
        numbers.append(int(sub))

    def is_prime(n):
        if n == 1:
            return False

        cnt = 0
        for i in range(2, n):
            if i * i > n:
                break
            if n % i == 0:
                cnt += 1
        if cnt == 0:
            return True
        else:
            return False

    result = 0
    for num in numbers:
        if is_prime(num):
            result += 1

    return result


print(solution(n, k))