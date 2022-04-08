from pathlib import Path

def get_complement(fasta: str):

    fasta = reversed(fasta)
    reverse_fasta = ''
    for base in fasta:
        if base == 'A':
            reverse_fasta += 'T'
        elif base == 'T':
            reverse_fasta += 'A'
        elif base == 'G':
            reverse_fasta += 'C'
        else:
            reverse_fasta += 'G'

    return reverse_fasta

dna:str = Path('rosalind_dna.txt').read_text()
print(get_complement(dna))