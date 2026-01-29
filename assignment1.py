import re


enzymes = {
    "DsaI": "CCRYGG",
    "SecI": "CCNNGG",
    "CjuI": "CAYNNNNNRTG"}


iupac = {
    "A": "A",
    "C": "C",
    "G": "G",
    "T": "T",
    "N": "[ACGT]",
    "R": "[AG]",
    "Y": "[CT]"
}


def to_regex(x):
    reg = ""
    for ch in x:
        reg += iupac[ch]
    return reg


def process(header, seq, pelet):
    found = False
    pelet_out = []  # אוסף את כל מה שנכתוב עבור הגן הזה

    for e in enzymes:
        regex = to_regex(enzymes[e])
        sites = re.findall(regex, seq)

        if len(sites) > 0:
            found = True
            pelet_out.append(f"\nThere are {len(sites)} {e} sites :\n")
            for site in sites:
                pelet_out.append(f"{e} site: {site}")

    if found:
        pelet.write(header + "\n")
        pelet.write("\n".join(pelet_out) + "\n\n.\n\n")

    return found


file1= open('orf_coding_all.fa.txt','r')
pelet=open('pelet.txt','w')
header=""
seq=""
count=0


for line in file1:
    line = line.strip()
    if line == "":
        continue

    if line.startswith(">"):
        if header != "":
            if process(header, seq, pelet):
                count += 1
        header = line
        seq = ""
    else:
        seq += line.upper()

if header != "":
    if process(header, seq, pelet):
        count += 1

pelet.write("Number of Protein with any kind of site: " + str(count) + "\n")

file1.close()
pelet.close()



