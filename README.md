# DNA-tools
small python tools for working with DNA sequences.
## reverse-complement.py
Takes a DNA sequence, replaces each base with its partner(A↔T, G↔C), and reverses the result.
example: 'GATTACA' gives 'TGTAATC'
## FASTA summariser.py
Reads a FASTA file, calculates the length and GC content of each sequence, and flags sequences longer than 1000 bases.
Example; run on the BRCA1 transcript(NM_007294.4), it reports a length of 7088 bases and GC content of 41.8%.
