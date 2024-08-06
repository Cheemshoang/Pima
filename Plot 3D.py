import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.cm as cm
import plotly.graph_objects as go
from InputmnNash import make_matrix
from InputmnNash import Nashnm


n, m = map(int, input().split())
w1,array1,w2,array2 = Nashnm(n,m)
A = make_matrix(n,m)
A_x = A.shape[0]
A_y = A.shape[1]
def payoff(arr1, arr2, matrix):
  """Calculates the expected payoff."""
  return arr1 @ matrix @ arr2.T

# Create a grid of probabilities
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)

# Calculate the expected payoff for each point on the grid
Z = np.zeros_like(X)
for i in range(len(x)):
    for j in range(len(y)):
        array1_copy = array1.copy()
        array1_copy.flat[A_x - 2] = x[i]
        array1_copy.flat[A_x - 1] = 1 - x[i]
        array2_copy = array2.copy()
        array2_copy.flat[(A_y//2)-1] = y[j]
        array2_copy.flat[A_y-1] = 1 - y[j]
        Z[i, j] = payoff(array1_copy, array2_copy, A)

# Create the Plotly surface plot
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])

# Add a colorbar
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))

# Nash_eq
nash_eq_x = array1[A_x - 2]
nash_eq_y = array2[(A_y)//2 -1]
nash_eq_z = payoff(array1, array2, A)
fig.add_trace(
    go.Scatter3d(
        x=[nash_eq_x],
        y=[nash_eq_y],
        z=[nash_eq_z],
        mode='markers',
        marker=dict(
            size=8,
            color='red',
            line=dict(
                color='red',
                width=2
            )
        ),
        name='Nash Equilibrium'
    )
)

#middle_point
array1_m = array1.copy()
array2_m = array2.copy()
array1_m.flat[A_x - 2] = 0.5
array1_m.flat[A_x - 1] = 0.5
array2_m.flat[(A_y)//2 -1] = 0.5
array2_m.flat[A_y-1] = 0.5
mid_z = payoff(array1_m, array2_m, A)

fig.add_trace(
    go.Scatter3d(
        x=[0.5],
        y=[0.5],
        z=[mid_z],
        mode='markers',
        marker=dict(
            size=8,
            color='blue',
            line=dict(
                color='blue',
                width=2
            )
        ),
        name='Middle'
    )
)

# Set labels and title
fig.update_layout(title='3D Expected Payoff', autosize=False,
                  width=800, height=800,
                  margin=dict(l=65, r=50, b=65, t=90),
                  scene=dict(
                    xaxis_title='Probability of Player 1 choosing n-1 (instead of n)',
                    yaxis_title='Probability of Player 2 choosing C (instead of L)',
                    zaxis_title='Expected Payoff'
                  ))

# Display the plot
fig.show()
