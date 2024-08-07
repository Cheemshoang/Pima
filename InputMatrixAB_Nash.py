import scipy.optimize as so
from scipy.optimize import linprog
import numpy as np
import nashpy as nash
from Inputmatrix import input_matrix
A = input_matrix()
B = input_matrix()
Nash = nash.Game(A,B)
a_0, b_0 = Nash.lemke_howson(initial_dropped_label=0)
print(a_0,b_0)
