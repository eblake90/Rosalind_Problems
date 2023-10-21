# https://rosalind.info/problems/mrna/
# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)


from functools import reduce
import operator


# Creating the RNA codonn dictionary
rna_codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',}

with open("C:\\Users\\Owner\\Downloads\\rosalind_mrna.txt", "r") as  file:
    protein_string = file.read().strip()

# Does not work with large protein strings due to stack overflow
"""
# finding the all the codon possibilies per amino acid
def inferrer(protein_string, rna_codon_table):
    
    rna_codons = []
    
    for amino_acid_unit in protein_string:
        
        amino_acid_matching = [codon for codon, AA in rna_codon_table.items() if AA == amino_acid_unit]
        
        rna_codons.append(amino_acid_matching)

    return rna_codons

# finding the all possible rna strings
def all_rna_sequences(rna_codons):
    
    if len(rna_codons) == 1:
        return rna_codons[0]
    
    sublists = all_rna_sequences(rna_codons[1:])
    
    return [codon + subseq for codon in rna_codons[0] for subseq in sublists]

"""       


# Do not run for large protien seq
#individaul_codon_possibilities = inferrer(protein_string, rna_codon_table)
#print("RNA sequence per AA:", individaul_codon_possibilities)


# Do not run for large protien seq
#rna_string_possibilities = all_rna_sequences(individaul_codon_possibilities)
#print("RNA full string possibilites:", rna_string_possibilities)
            

# Initiate dictionary for counting the codons assicated with the found amino acids
codon_count = {}

# Count the number of codons for each amino acid in rna codon table
for codon, AA in rna_codon_table.items():
        codon_count[AA] = codon_count.get(AA, 0) + 1

product = 1

# For each amino acid in the protein string
for amino_acid in protein_string:
    # Multiply the current product with the number of codons for that amino acid
    product *= codon_count[amino_acid]

# Multiply with the number of stop codons
product *= codon_count["Stop"]

# Take the result modulo 1,000,000
number_of_strings_corrected = product % 1000000

#number_of_strings = reduce(operator.mul, codon_count.values()) % 1000000

print("Number of possible RNA strings:", number_of_strings_corrected)
#print("Protein String:", protein_string)
print("Codon Count:", codon_count)



