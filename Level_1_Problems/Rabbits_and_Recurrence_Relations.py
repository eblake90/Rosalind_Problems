def rabbit_pairs(n, k):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rabbit_pairs(n-1, k) + k * rabbit_pairs(n-2, k)


n = 31
k = 2

print(rabbit_pairs(n, k))