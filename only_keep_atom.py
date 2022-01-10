"""
@ Description: Only keep line starts with ATOM in a pdb file
@ Author: Shawn Chen
@ Date : 2020-01-10

Usage:
    The input and output could keep same
"""


import os
import sys

input_pdb = os.path.abspath(sys.argv[1])
output_pdb = os.path.abspath(sys.argv[2])

records = ('ATOM')

with open(input_pdb, 'r') as f:
    content = f.readlines()
    f.close()

new_content = []
for i in content:
    if i.startswith(records):
        new_content.append(i)

with open(output_pdb, 'w') as f:
    for i in new_content:
        i.strip('\n')
        f.write(i)
    f.close()
