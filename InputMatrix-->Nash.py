import scipy.optimize as so
from scipy.optimize import linprog
import numpy as np


def input_matrix():
    matrix = []

    while True:
        row = input()
        if not row:
            break
        matrix.append(list(map(float, row.split())))

    return matrix


matrix_list = input_matrix()
matrix_np = np.array(matrix_list)
min_value = np.min(matrix_np)
matrix_np = matrix_np - min_value + 1
x,y = matrix_np.shape
#P1
c = np.ones(x)
A_ub = -matrix_np.T
b_ub = -np.ones(y)


A_eq = None
b_eq = None

bounds = [
    (0, None)
    for i in range(len(c))
]

result = linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=bounds,
)


if result.success:
  w = 1/result.fun
  array1 = w * result.x
  w = w + min_value - 1
  print("v_1 = ", w)
  print("X_0", array1)
else:  print("No solution found. The problem might be infeasible or unbounded.")


#P2
c = -np.ones(y)


A_ub = matrix_np
b_ub = np.ones(x)


A_eq = None
b_eq = None


bounds = [
    (0, None)
    for i in range(len(c))
]


result = linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub,
    A_eq=A_eq,
    b_eq=b_eq,
    bounds=bounds,
)


if result.success:
  w = -1/result.fun
  array2 = w * result.x
  w = w + min_value - 1
  print("v_2 = ", w)
  print("Y_0" , array2)
else:
  print("No solution found. The problem might be infeasible or unbounded.")
