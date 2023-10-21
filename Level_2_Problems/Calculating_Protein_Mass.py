# https://rosalind.info/problems/prtm/
# Given: A protein string P of length at most 1000 aa.
# Return: The total weight of P. Consult the monoisotopic mass table.


# monoisotopic mass table
# Creating a dictionary based on the provided data
amino_acid_masses = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}

with open("C:\\Users\\eblak\\Downloads\\rosalind_prtm.txt", "r") as  file:
    protein_string = file.read().strip()
 
protein_mass = 0

# Finding the mass of the given protein string using the monoisotopic mass table
for amino_acid in protein_string:
    if amino_acid in amino_acid_masses:
        protein_mass += amino_acid_masses[amino_acid]
        
print("The protein string mass is:", protein_mass)










