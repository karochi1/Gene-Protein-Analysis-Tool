#provides analysis on DNA sequences

def ATGC_content(DNA):  #returns ATGC contents in the form of a dict

    ATGCDict = {'A' : 0,
                'T': 0,
                'G' : 0,
                'C' : 0}
    for nucleotide in DNA:
        if nucleotide == 'A':
            ATGCDict['A'] += 1
        elif nucleotide == 'T':
            ATGCDict['T'] += 1
        elif nucleotide == 'G':
            ATGCDict['G'] += 1
        else:
            ATGCDict['C'] += 1
    return ATGCDict

#todo: hamming differences, complementary base pair completer