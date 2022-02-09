"""
@ Description: read sequence
@ Author: Shawn
@ Date: 2022-01-11
"""

def read_fasta(fasta_file: str):
    with open(fasta_file) as f:
        content = f.readlines()
        f.close()
    seq = ''
    for i in content:
        if not(i.startswith('>')):
            seq += i.strip()
            return seq
        else:
            target_id, length = i.split('|')
            target_id = target_id.strip().strip('>')
            length = length.strip()
            return target_id, length, seq
