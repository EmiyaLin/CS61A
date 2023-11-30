def multiply(m, n):
    if n == 1:
        return m
    return m + multiply(m, n - 1)

def skip_mul(n):
    if n == 1 or n == 2:
        return n
    return n * skip_mul(n - 2)

def is_prime(n):
    def judge(m, n):
        if m == 1:
            return False
        elif m == n:
            return True
        elif n % m == 0:
            return False
        else:
            return judge(m + 1, n)

    if n == 2:
        return True
    else:
        return judge(2, n)

def hailstone(n):
    def func(n, m):
        print(n)
        if n == 1:
            return m
        if n % 2 == 0:
            return func(n // 2, m + 1)
        return func(n * 3 + 1, m + 1)

    return func(n, 1)

def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    if n1 % 10 > n2 % 10:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    if n1 % 10 <= n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
