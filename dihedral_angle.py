"""
@ Description: Run biopython for dihedral angle
@ Author: Shaw Chen
@ Date: 2022-01-12
"""


import os
import Bio.PDB
from typing import List
from pdb_tofasta import pdb2fasta

def get_dihedral_angle(pdb_file: str) -> List:
    tmp_list = []
    
    for model in Bio.PDB.PDBParser().get_structure(pdb_file.split('/')[-1].split('.')[0], pdb_file):
        for chain in model:
            poly = Bio.PDB.Polypeptide.Polypeptide(chain)
            tmp_list.append(poly.get_phi_psi_list())

    angle_list = []
    for i in tmp_list:
        for j in i:
            angle_list.append(i)

    return angle_list

