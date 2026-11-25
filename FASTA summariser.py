import urllib.request

url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NM_007294&rettype=fasta&retmode=text"
urllib.request.urlretrieve(url, "brca1.fasta")

current = ""
genes = {}

with open("brca1.fasta") as f:
    for line in f:
        if line.startswith(">"):
            current = line.strip()[1:]
            genes[current] = ""
        else:
            genes[current] += line.strip()

print("Gene report")
print("-" * 40)

passing = []

for name, seq in genes.items():
    length = len(seq)
    gc = (seq.count("G") + seq.count("C")) / length * 100

    if length > 1000:
        status = "PASS"
        passing.append(name)
    else:
        status = "SHORT"

    print(name[:20], "| length:", length, "| GC:", round(gc, 1), "% |", status)

print("Passing genes:", passing)
