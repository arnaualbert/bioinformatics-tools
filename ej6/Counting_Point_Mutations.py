from pathlib import Path

def get_points_mutation(fasta: str):

    lines: str = fasta.split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    counter = 0

    for point in range(len(seq_one)):
        if seq_two[point] != seq_one[point]:
            counter = counter + 1

    return counter


dna:str = Path('rosalind_dna.txt').read_text()
print(get_points_mutation(dna))