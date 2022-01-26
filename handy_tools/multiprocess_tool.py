"""
@ Description: Wrapper for multiprocessing
@ Author: Shawn Chen
@ Date: 2022-01-15
"""


import multiprocessing as mp


def mp_wrapper(func, args_list, threads=-1):
    if threads == -1:
        threads = mp.cpu_count()

    print('Parallel Mode: Using %d threads for writing.', threads)

    if threads == 1:
        print('Sequential Mode')

    p = mp.Pool(threads)
    for args in args_list:
        p.apply_async(func, args)
    
    p.close()
    p.join()
    print('Finished')

    return None
