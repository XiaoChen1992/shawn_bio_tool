"""
@ Description: read sequence
@ Author: Shawn
@ Date: 2022-01-11
"""

def read_fasta(fasta_file: str) -> str:
    with open(fasta_file) as f:
        content = f.readlines()
        f.close()
    seq = ''
    for i in content:
        if not(i.startswith('>')):
            seq += i.strip()
    return seq
