
# Input: ATGCCCTAG
# OUTPUT: AUGCCCUAG

def dna_to_rna(gene):

    rna = []
    for base in gene:

        if base == "T":
            rna.append("U")

        else:
            rna.append(base)

    return ''.join(rna)


assert(dna_to_rna('ATGCCCTAG') == "AUGCCCUAG")
assert(dna_to_rna('') == '')

def rna_to_protein(rna):


    CODON_TO_AA = {
        'UUU': 'F',
        'UUC': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'UAU': 'Y',
        'UAC': 'Y',
        'UAA': '*',
        'UAG': '*',
        'UGU': 'C',
        'UGC': 'C',
        'UGA': '*',
        'UGG': 'W',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'AGU': 'S',
        'AGC': 'S',
        'AGA': 'R',
        'AGG': 'R',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G',
    }

    protein = []

    for index in range(0, len(rna), 3):

        codon = rna[index:index+3]
        if codon in CODON_TO_AA:
            protein.append(CODON_TO_AA[codon])

    return ''.join(protein)

assert(rna_to_protein('GGGGAGGUU')== 'GEV')
assert(rna_to_protein('GGGGAGUU')== 'GE')


def trim_at_stop(protein):

    if '*' not in protein:
        return None

    frame = protein.split('*')

    return ''.join(frame[0]) + '*'

assert(trim_at_stop('GEV*E') == 'GEV*')
assert(trim_at_stop('GEV') == None)


def open_reading_frame(dna):

    rna = dna_to_rna(dna)

    frames = []

    for i in range(len(rna)):

        if rna[i:i+3] == "AUG":
            
            current = rna_to_protein(rna[i:])

            trimmed = trim_at_stop(current)

            if trimmed:
                frames.append(trimmed)


    return frames

assert(open_reading_frame('ATGCATGCCTAGCTAG') == ['MHA*', 'MPS*'])

assert(open_reading_frame('ATGATGTAG') == ['MM*', 'M*'])

assert(open_reading_frame('') == [])

MMMMMMMM*
MMMMMMM*
M*

#keep track of all stars and then look for ms before it

print('passed!')