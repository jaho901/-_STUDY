import sys
sys.stdin = open('2023.txt')

'''
10**8승이기 때문에 에라토스테네스의 체는 시간초과가 발생한다.
=> 이런 경우는 소수 판별 방법을 사용해서 소수인지를 구해야 한다.
'''

n = int(input())

def is_prime(prime_num):
    if prime_num == 1:
        return False
    for i in range(2, prime_num):
        if i * i > prime_num:
            break
        if prime_num % i == 0:
            return False
    return True

def dfs(num):
    # n 자리수까지 체크하게 되면 1~n자리 모두 소수이니 출력한다.
    if len(str(num)) == n:
        print(num)

    else:
        for i in range(10):
            sub = num*10 + i
            if is_prime(sub):
                dfs(sub)

# 2, 3, 5, 7을 체크하는 이유는 일의자리수 중 소수가 2,3,5,7이기 때문이다.
# 여기서 10을 곱하기 0~9까지 더해주면서 소수를 계속해서 찾아가는 과정이다.
dfs(2)
dfs(3)
dfs(5)
dfs(7)