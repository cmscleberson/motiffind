

import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'apyori'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'biopython'])


    

from Bio import SeqIO
from apyori import apriori   
    

def readSequences(fileIn):
    listSequences = []
    for i in SeqIO.parse(fileIn, "fasta"):
        listSequences.append(list(i.seq))
    return listSequences


def sepSeq(seqIn):
    listOut=[]
    for i in range(seqIn):
        listOut.append(seqIn[i])
    return listOut


seq1 = readSequences('camelus.fas')
seq2 = readSequences('musmusc.fas')

seqFinal = list(seq1+seq2)


rules = apriori(seqFinal, min_support=0.1, min_confidence=0.2, min_lift=1, min_length=1)
association_results = list(rules)

output_file = open('outassociations.txt', 'w')

for rule in association_results:
    output_file.write(rule + '\n')

output_file.close()



