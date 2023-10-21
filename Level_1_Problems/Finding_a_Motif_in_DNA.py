
with open("C:\\Users\\eblak\\Downloads\\rosalind_subs.txt", "r") as  file:
    s = file.readline().strip()
    t = file.readline().strip()

locations = []

for i in range(0, len(s)):
    if t == s[i:i+len(t)]:
        
        locations.append(i+1)
    else:
        continue

print(locations)
        