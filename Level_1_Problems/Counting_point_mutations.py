with open("C:\\Users\\eblak\\Downloads\\rosalind_hamm.txt", "r") as  file:
    s = file.readline().strip()
    t = file.readline().strip()

hamming_distance = 0

for i in range(0, len(s)):
    if s[i] != t[i]:
        hamming_distance += 1

print(hamming_distance)
