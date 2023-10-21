
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
    
    




