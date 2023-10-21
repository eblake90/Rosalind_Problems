# https://rosalind.info/problems/revc/
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement s^c of s.

import collections
import  random

with open("C:\\Users\\eblak\\Downloads\\rosalind_revc.txt", "r") as  file:
    DNA_string = file.read().strip()
    
    
reverse_complement = []

for i in DNA_string:
    if i == "T":
        reverse_complement.append("A")
    if i == "A":
        reverse_complement.append("T")
    if i == "C":
        reverse_complement.append("G")
    if i == "G":
        reverse_complement.append("C")
       

print("Original: ", DNA_string)
print("Reverse Complement: ", "".join(reverse_complement)[::-1])
      
      
