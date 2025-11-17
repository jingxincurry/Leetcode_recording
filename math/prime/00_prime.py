"""
质数



"""
from math import isqrt
# 时间复杂度 O(sqrt(n))
# 等价于   is_prime = lambda n: n >= 2 and all(n % i for i in range(2, isqrt(n) + 1))

def is_prime(n: int) -> bool:
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2  # 1 不是质数

# 时间复杂度 O(MX * log log MX)
# 埃氏筛
def sieve(MX=1_000_001):
    """返回 0 ~ MX-1 内所有质数的列表"""
    is_prime = [False] * 2 + [True] * (MX - 2)  # 0 和 1 不是质数
    primes = []
    for i in range(2, MX):
        if is_prime[i]:
            primes.append(i)
            # 从 i*i 开始筛掉 i 的倍数
            for j in range(i * i, MX, i):
                is_prime[j] = False
    return primes

# 质因数分解
def prime_factorization(n: int) -> dict:
    """返回 n 的质因数分解结果，格式为 {质因数: 指数}"""
    
    prime_factors = [[] for _ in range(n)]
    for i in range(2, n):
        if not prime_factors[i]:  # i 是质数
            for j in range(i, n, i):  # i 的倍数 j 有质因子 i
                prime_factors[j].append(i)
    



if __name__ == "__main__":

    print(sieve(10))
  
    print(is_prime(11))  # True
    print(is_prime(15))  # False