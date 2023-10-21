import collections
import  random

with open("C:\\Users\\eblak\\Downloads\\rosalind_dna (3).txt", "r") as  file:
    DNA_string = file.read().strip()

print(collections.Counter(DNA_string))

