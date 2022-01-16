"""
@ Description: Remove TER line
@ Author: Shawn Chen
@ Date: 2022-01-16
"""


def DeleteTER(src_pdb_file: str, dst_pdb_file: str) -> None:
    """remove TER line"""
    fhandle = open(src_pdb_file, 'r')
    records = 'TER'
    new_line = []
    for line in fhandle:
        if line.startswith(records):
            continue
        new_line.append(line)
    open(dst_pdb_file, 'w').write(''.join(new_line))

    return None