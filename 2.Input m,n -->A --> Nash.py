import scipy.optimize as so
from scipy.optimize import linprog
import numpy as np

n,m = input().split()
n = int(n)
m = int(m)
print(n,m)
A = np.zeros((n+1,2*m+1))
def make_matrix(n,m):
  even = True
  if n%2 == 1:
    n = n+1
    even = False
  A = np.zeros((n+1,2*m+1))
  for k in range(1,n+1):
    for t in range(1,2*m+1):
      if k%2 == 0 and 1 <= t <= m:
        A[k][t] =  -t
      elif k%2 == 0 and m+1 <= t <= 2*m:
        A[k][t] = k
      elif k%2 == 1 and 1 <= t <= m:
        A[k][t] = k
      elif k%2 == 1 and m+1 <= t <= 2*m:
        A[k][t] = m-t
  A = A[1:]
  A = A[:,1:]
  if even == False:
    A = A[:-1]
  return A

matrix_np = make_matrix(n,m)
min_value = np.min(matrix_np)
matrix_np = matrix_np - min_value + 1
x,y  = matrix_np.shape
# for i in range(x):
#   for j in range(y):
#     matrix_np[i][j] += matrix_np[x-1][y-1] +1

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
