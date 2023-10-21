# https://rosalind.info/problems/fib/
# Given: Positive integers n≤40 and k≤5.
# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).


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
