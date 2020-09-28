import numpy as np

root_3_inverse = 3**-0.5
one_third = 1/3

identity = np.identity(3)
ones = np.ones(3)
final_matrix = [
    [0, -root_3_inverse, root_3_inverse],
    [root_3_inverse, 0, -root_3_inverse],
    [-root_3_inverse, root_3_inverse, 0]
]
final_matrix = np.array(final_matrix)


def rotation(angle):
    return identity*np.cos(angle) + 0.5*ones*(1 - np.cos(angle)) + final_matrix*np.sin(angle)
