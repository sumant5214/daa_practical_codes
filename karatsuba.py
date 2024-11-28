def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        m = n // 2
        divisor = 10 ** m
        a = x // divisor
        b = x % divisor
        c = y // divisor
        d = y % divisor
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        return (ac * (10 ** (2 * m))) + (ad_plus_bc * (10 ** m)) + bd

x = 5678
y = 1234

result = karatsuba(x, y)
print(result)
