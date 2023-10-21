
n = 86 # number of months
m = 18 # number of months each pair of rabbits live for
k = 1  # starting pair

def rabbit_count(n, k, m):
    
    rabbits =  [0] * m
    
    # Starting pair
    rabbits[0] = k
    
    for months in range(1, n):
        
        # Calculating new offspring
        new_rabbits = k * sum(rabbits[1:])
    
        # Adding the new rabbits and removing those passed 3 months
        rabbitss = [new_rabbits] + rabbits[:-1]
    
    return sum(rabbits)


print(f"After {n} months {rabbit_count(n, k, m)} pairs remain")