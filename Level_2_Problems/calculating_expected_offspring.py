# https://rosalind.info/problems/iev/
# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.

with open("C:\\Users\\eblak\\Downloads\\rosalind_iev.txt", "r") as  file:
    couples_used = file.read()

couples_used = {"AA-AA": 17797,
                "AA-Aa": 19651,
                "AA-aa": 18763,
                "Aa-Aa": 16672,
                "Aa-aa": 16072,
                "aa-aa": 16973}
    
dominant_prob = {"AA-AA": 2,
                "AA-Aa": 2,
                "AA-aa": 2,
                "Aa-Aa": 1.5,
                "Aa-aa": 1,
                "aa-aa": 0}

result = 0

for i in couples_used:
    result += couples_used[i] * dominant_prob[i]

print("The expected number:", result)
    
    




