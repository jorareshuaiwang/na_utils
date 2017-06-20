"""
convert DNA seq to RNA
"""

def rna(seq):
    """convert RNA to DNA"""
    #determine if the sequence is upper case
    seq_upper = seq.isupper()

    #convert to lowercase
    seq = seq.lower()

    #swap
    seq = seq.replace('t','u')

    #return upper or lower,depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_comp(seq):
    """convert a DNA to reverse complement as RNA"""
    # determine if original was upper
    seq_upper = seq.isupper()

    # reverse_rna_comp
    seq = seq[::-1]

    #compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G','c')
    seq = seq.replace('C', 'g')

    #return in case
    if seq_upper:
        return seq.upper()
        return seq
