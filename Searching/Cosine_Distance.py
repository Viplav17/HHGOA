import numpy as np

def cosine_distance(vec_a, vec_b):
    a = np.array(vec_a)
    b = np.array(vec_b)
    return 1.0 - (np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))