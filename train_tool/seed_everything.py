"""
@ Description: set seed fo random, numpy, torch and cuda
@ Author: Shawn Chen
@ Date: 2022-01-26
"""

import random
import numpy as np
import torch

def seed_everything(seed=666):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
    return None