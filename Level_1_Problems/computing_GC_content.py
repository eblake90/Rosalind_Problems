# Reading the fasta file
def read_genome(txtfile):
    genome = {}
    
    with open(txtfile, "r") as x:
        for line in x:
            if line[0] == ">":
                genome_location = line[1:].rstrip()
                genome[genome_location] = ""
                
            else:
                genome[genome_location] += line.rstrip()
                
    return genome
 

# Read the genome from the downloaded file.
genome = read_genome("C:\\Users\\eblak\\Downloads\\rosalind_gc (1).txt")

# Checking if read_genome function works
for  genome_location,  sequence in genome.items():
    print(f"{genome_location}: {sequence}\n")

# Finding GC-content 
GC_list  = []
for genome_location, sequence in genome.items():
    print("Sequence", genome_location, ":", sequence)

    GC_content = 0
    
    for i in range(len(sequence)-1):
        if sequence[i] == "G" or sequence[i] == "C":
            GC_content += 1
   
    GC_percentage = ((GC_content)/len(sequence)) * 100

    GC_list.append((genome_location, GC_percentage))
    
# Sorting GC_list from lowest to highest GC percentage

sort_GC_list = sorted(GC_list,  key=lambda x: x[1])
    
for genome_location, GC_content in sort_GC_list:
    print(f"Sequence Counter of {genome_location}: {GC_content:.6f}%")



