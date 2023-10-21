# https://rosalind.info/problems/hamm/
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance d_H (s,t).


with open("C:\\Users\\eblak\\Downloads\\rosalind_hamm.txt", "r") as  file:
    s = file.readline().strip()
    t = file.readline().strip()

hamming_distance = 0

# Finding mismatches along both strings
for i in range(0, len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)
