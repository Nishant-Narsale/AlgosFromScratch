import numpy as np
import pandas as pd

def relu(z: np.array) -> np.array:
    return np.maximum(0, z)