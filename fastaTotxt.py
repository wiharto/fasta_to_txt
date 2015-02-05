# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 10:56:01 2015

@author: patriciawiharto
"""

import re

def convert(file1, file2='convertedFile.txt'):
    """
    @param file1: input (.fa file to be converted).
    @param file2: output (.txt file).
    @return: a .txt file named 'convertedFile.txt' by default.
    """

    seq_name = ''

    # Open file1 and file2 and assign to fOut and fIn respectively
    with open(file1, 'r') as fOut, open(file2, 'w') as fIn:

        # Read each line from file1
        for line in fOut:
            fasta_match = re.match('>', line)            # match for fasta '>' character
            if fasta_match:
                seq_name = line.lstrip('>').rstrip('\n') # assign sequence name to seq_name
            else:
                seq = line                               # assign DNA sequence to seq
                fIn.write(seq_name + ',' + seq)          # write seq_name and seq separated by comma to file2.txt
    fOut.close()
    fIn.close()


"""

Test code

"""

convert('ref_transcripts.fa')
