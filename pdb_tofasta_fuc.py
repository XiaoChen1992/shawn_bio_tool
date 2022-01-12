"""
@ Description: Extract sequence from pdb file as a python function
@ Author: Shawn Chen
@ Create date: 2022-01-09

Only consiser ATOM.
"""


import os
import sys


def pdb2fasta(pdb_file):
    """
    Args:
        pdb_file: pdb file path
    Returns:
        sequence
    """

    
    amino = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N',
        'ASP': 'D', 'CYS': 'C', 'GLU': 'E',
        'GLN': 'Q', 'GLY': 'G', 'HIS': 'H',
        'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
        'MET': 'M', 'PHE': 'F', 'PRO': 'P',
        'SER': 'S', 'THR': 'T', 'TRP': 'W',
        'TYR': 'Y', 'VAL': 'V'}

    if not os.path.isfile(pdb_file):
        print(f'Please check {pdb_file}')
        sys.exit(1)

    with open(pdb_file, 'r') as f:
        content = f.readlines()
    f.close()
    seq = []
    prev_mark = -1
    for line in content:
        if line[:4] == 'ATOM':
            pos_mark = line[22: 26].strip()
            if pos_mark != prev_mark:
                seq.append(amino[line[17:20]])
            prev_mark = pos_mark
    return "".join(seq)