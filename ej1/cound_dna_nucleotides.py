from pathlib import Path

def get_dna_nucleotides(fasta: str):

    a = fasta.count('A')
    t = fasta.count('T')
    c = fasta.count('C')
    g = fasta.count('G')

    return a,c,g,t

dna:str = Path('rosalind_dna.txt').read_text()
print(get_dna_nucleotides(dna))