"""
@ Description: Generate distance map from a pdb file
@ Author: Shawn
@ Date: 2022-01-11
"""


import os
import numpy as np
from argparse import ArgumentParser
from sklearn.metrics.pairwise import euclidean_distances
from biopandas.pdb import PandasPdb

parser = ArgumentParser(description='Generate distance map from a pdb file')
parser.add_argument('--pdb', '-p', type=str, required=True)
parser.add_argument('--name', '-n', type=str, required=True)
parser.add_argument('--output', '-o', type=str, required=True)
parser.add_argument('--atom', '-a', type=str, default='CB', required=False)
args = parser.parse_args()

pdb_file = args.pdb
pdb_name = args.name
output_folder = args.output
atom_type = args.atom


def distance_helper(pdb_file: str, pdb_name: str, output_folder: str, atom_type='CB') -> None:
    ppdb = PandasPdb().read_pdb(pdb_file)
    test_df = ppdb.df['ATOM']

    if atom_type == 'CB':
        # GLY does not have CB, use CA to instead of.
        filtered_df = test_df[((test_df.loc[:, 'residue_name'] == 'GLY') & (test_df.loc[:, 'atom_name'] == 'CA')) \
                              | (test_df.loc[:, 'atom_name'] == 'CB')]
    elif atom_type == 'CA':
        filtered_df = test_df[test_df.loc[:, 'atom_name'] == 'CA']
    elif atom_type == 'NO':
        filtered_df = test_df[(test_df.loc[:, 'atom_name'] == 'N') | (test_df.loc[:, 'atom_name'] == 'O')]
    else:
        raise ValueError('Atom type should be CA, CB or NO.')

    if atom_type != 'NO':
        coord = filtered_df.loc[:, ['x_coord', 'y_coord', 'z_coord']].values.tolist()
        real_dist = euclidean_distances(coord)
    else:
        coord_N = filtered_df[filtered_df.loc[:, 'atom_name'] == 'N'].loc[:, ['x_coord', 'y_coord', 'z_coord']].values.tolist()
        coord_O = filtered_df[filtered_df.loc[:, 'atom_name'] == 'O'].loc[:, ['x_coord', 'y_coord', 'z_coord']].values.tolist()
        real_dist = euclidean_distances(coord_N, coord_O)  # up-triangle N-O, low-triangle O-N
        np.fill_diagonal(real_dist, 0)  # set diagnoal value to 0
    
    # # get full N-O distance map and O-N distance map
    # e_1 = np.identity(real_dist.shape[0])[:,::1]
    # no_distance = np.triu(real_dist)
    # no_mirror = e_1.dot(no_distance.T).dot(e_1)
    # no_full = no_mirror + no_distance

    # on_distance = np.tril(real_dist)
    # on_mirror = e_1.dot(on_distance.T).dot(e_1)
    # on_full = on_mirror + on_distance
    
    real_dist = np.round(real_dist, 3)


    np.save(file=os.path.join(output_folder, pdb_name + f'_{atom_type}.npy'),
            arr=real_dist)
    return None


if __name__ == '__main__':
    distance_helper(pdb_file, pdb_name, output_folder, atom_type)
