def input_matrix():
    matrix = []

    while True:
        row = input()
        if not row:
            break
        matrix.append(list(map(float, row.split())))

    return matrix



def Nash(matrix_list):
  output = []
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

#Main
matrix = input_matrix()
Nash(matrix)
