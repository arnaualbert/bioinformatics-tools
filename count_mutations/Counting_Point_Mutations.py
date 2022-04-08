from pathlib import Path

def get_points_mutation(fasta: str):

    # separate the the sequences
    lines: str = fasta.split("\n")

    seq_one = lines[0]
    seq_two = lines[1]

    # put the counter at 0
    counter = 0

    # compare the first sequence with the second sequence and print the number of total difereces between the sequences
    for point in range(len(seq_one)):
        if seq_two[point] != seq_one[point]:
            counter = counter + 1

    return counter


dna:str = Path('rosalind_dna.txt').read_text()
print(get_points_mutation(dna))