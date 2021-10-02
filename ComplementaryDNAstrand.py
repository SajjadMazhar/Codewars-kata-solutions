# A=T C=G

def DNA_strand(dna):
    strand_pair={'A':'T','T':'A', 'C':'G', 'G':'C'}
    for strand in dna:
        print(strand_pair[strand], end='')

DNA_strand('AAAA')