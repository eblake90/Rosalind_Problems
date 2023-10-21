# https://rosalind.info/problems/dna/
# Given: A DNA string s of length at most 1000 nt
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

import collections
import  random

with open("C:\\Users\\eblak\\Downloads\\rosalind_dna (3).txt", "r") as  file:
    DNA_string = file.read().strip()

print(collections.Counter(DNA_string))

