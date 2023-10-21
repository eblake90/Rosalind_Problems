# https://rosalind.info/problems/subs/
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.


# Given values
k, m, n = 2, 2, 2
total_population = k + m + n

# Calculate probabilities of each mating pair
prob_kk = (k/total_population) * ((k-1)/(total_population-1))
prob_km = (k/total_population) * (m/(total_population-1)) + (m/total_population) * (k/(total_population-1))
prob_kn = (k/total_population) * (n/(total_population-1)) + (n/total_population) * (k/(total_population-1))
prob_mm = (m/total_population) * ((m-1)/(total_population-1))
prob_mn = (m/total_population) * (n/(total_population-1)) + (n/total_population) * (m/(total_population-1))
prob_nn = (n/total_population) * ((n-1)/(total_population-1))

# Calculate total probability of offspring having a dominant allele
probability_dominant = (
    prob_kk * 1 +
    prob_km * 1 +
    prob_kn * 1 +
    prob_mm * 0.75 +
    prob_mn * 0.5 +
    prob_nn * 0
)

print("Probability of Daminace:", probability_dominant)
