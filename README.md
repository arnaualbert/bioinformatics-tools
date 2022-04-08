# Bioinformatics Tools

# Indice

## - [Counting DNA Nucleotides](#Counting-DNA-Nucleotides)

## - [Transcribing DNA into RNA](#Transcribing-DNA-into-RNA)

## - [Complementing a Strand of DNA](#Complementing-a-Strand-of-DNA)

## - [Counting Point Mutations](#Counting-Point-Mutations)

# Counting DNA Nucleotides 

A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s

of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

### - [Ir al índice](#Indice).

# Transcribing DNA into RNA

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t

having length at most 1000 nt.

Return: The transcribed RNA string of t.

### - [Ir al índice](#Indice).

# Complementing a Strand of DNA

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
is the string sc formed by reversing the symbols of s

, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s

of length at most 1000 bp.

Return: The reverse complement sc
of s.

### - [Ir al índice](#Indice).

# Counting Point Mutations

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

. See Figure 2.

Given: Two DNA strings s
and t

of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).

### - [Ir al índice](#Indice).
