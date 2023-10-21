# https://rosalind.info/problems/lia/
# Given: Two positive integers k(k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.
# Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors

from math import comb

# function to factor in k^th generations
def generation_k(genome_probs, k):
    prob = 1
    
    for i in genome_probs:
        prob *= genome_probs[i]
    
    return prob

# function to finnd the probability of genotype after k^th generations
def genotype_prob(genome_probs, k, n):
    
    # probability of AaBa after mating
    p = generation_k(genome_probs, k)
    
    # Total number of organism in k^th generation
    N = 2 ** k
       
    total_prob = 0
    
    for i in range(n,  N+1):
        total_prob += comb(N, i) * (p**i) * ((1-p)**(N-i))

    return total_prob

# Given values
k = 5
n = 7

# Probabilities for Aa-Aa // Ba-Ba alleles
genome_prob_Aa_Aa = {"AA": 0.25,
                     "Aa": 0.5,
                     "aa": 0.25}

genome_prob_Bb_Bb = {"BB": 0.25,
                     "Bb": 0.5,
                     "bb": 0.25}

# Finding the genome probability of having offspring with Aa and Ba
genome_probs = {"Aa": genome_prob_Aa_Aa["Aa"],
                "Bb": genome_prob_Bb_Bb["Bb"]}

print("The probability of getting AaBa is:", genotype_prob(genome_probs, k, n))
