import scipy.optimize as so
from scipy.optimize import linprog
import numpy as np

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

def Nashnm(n,m):
  A = np.zeros((n+1,2*m+1))
  matrix_np = make_matrix(n,m)
  min_value = np.min(matrix_np)
  matrix_np = matrix_np - min_value + 1
  x,y  = matrix_np.shape


  output = []
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
    w1 = 1/result.fun
    array1 = w1 * result.x
    w1 = w1 + min_value - 1
    output.append(w1)
    output.append(array1)
  else:
    print("No solution found. The problem might be infeasible or unbounded.")
    return


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
    w2 = -1/result.fun
    array2 = w2 * result.x
    w2 = w2 + min_value - 1
    output.append(w2)
    output.append(array2)
  else:
    print("No solution found. The problem might be infeasible or unbounded.")
    return
  return output
  
#main
n, m = map(int, input().split())
Nashnm(n,m)
