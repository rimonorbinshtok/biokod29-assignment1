import re
file= open('orf_coding_all.fa.txt','r')
pelet=open('pelet.txt','w')
header=""
seq=""
for line in file:
    line=line.strip()
    if line.startswith('>'):
        if header!="":
            pelet.write(header+'\n')
            pelet.write(seq+'\n')
        header=line
        seq=""
    else:
        seq+=line
pelet.write(header+'\n')
pelet.write(seq+'\n')


seq = "AACCGTGGCCATGG"
pattern = "CC[AG][CT]GG"
