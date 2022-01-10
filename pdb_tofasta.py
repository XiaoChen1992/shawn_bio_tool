"""
@ Description: Extract sequence from pdb file
@ Author: Shawn Chen
@ Create date: 2020-10-21

Only consiser ATOM.
Example:
    python pdb_tofasta.py XXXX.pdb XXXX ./output
"""


import os
import sys

amino = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N',
         'ASP': 'D', 'CYS': 'C', 'GLU': 'E',
         'GLN': 'Q', 'GLY': 'G', 'HIS': 'H',
         'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
         'MET': 'M', 'PHE': 'F', 'PRO': 'P',
         'SER': 'S', 'THR': 'T', 'TRP': 'W',
         'TYR': 'Y', 'VAL': 'V'}


def pdb2fasta(pdb_file):
    """
    Args:
        pdb_file: pdb file path
    Returns:
        sequence
    """
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


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Required input pdb file, target name and output folder')
        sys.exit(1)
    sequence = pdb2fasta(os.path.abspath(sys.argv[1]))
    print(sequence)
    target_id = sys.argv[2]
    output_folder = os.path.abspath(sys.argv[3])
    with open(f'{output_folder}/{target_id}.fasta', 'w') as f:
        f.writelines(f'>{target_id} | {len(sequence)}')
        f.writelines('\n')
        f.writelines(sequence)
    f.close()