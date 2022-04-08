from pathlib import Path

def get_transcription(fasta: str):

    # change the T to U
    transcription = fasta.replace('T','U')

    return transcription

dna:str = Path('rosalind_dna.txt').read_text()
print(get_transcription(dna))