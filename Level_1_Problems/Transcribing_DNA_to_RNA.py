import collections
import  random

with open("C:\\Users\\eblak\\Downloads\\rosalind_rna.txt", "r") as  file:
    DNA_string = file.read().strip()


RNA_string = str.replace(DNA_string, "T", "U")

print(RNA_string)
    
    