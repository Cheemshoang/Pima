import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from InputmnNash import make_matrix
import matplotlib.cm as cm

A = make_matrix(n,m)
A_x = A.shape[0]
A_y = A.shape[1]

def payoff(arr1, arr2, matrix):
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

# Plot the expected payoffs
fig, ax = plt.subplots()
cmap = cm.RdBu
norm = Normalize(vmin=Z.min(), vmax=Z.max())  # Normalize based on calculated payoffs
contour = ax.contourf(X, Y, Z, levels=100, cmap=cmap, norm=norm)

# Add a colorbar
cbar = plt.colorbar(contour)
cbar.set_label('Expected Payoff')

#middle
middle_x = 0.5
middle_y = 0.5
ax.plot(middle_x, middle_y, 'ro', label='Middle', color = 'blue')

#nash
nash_eq_x = array1[A_x - 2]
nash_eq_y = array2[(A_y)//2 -1]
ax.plot(nash_eq_x, nash_eq_y, 'ro', label='Nash Eq', color = 'red')

#p1 0.5 p2 nash
x_1 = 0.5
y_1 = array2[(A_y)//2 -1]
ax.plot(x_1, y_1, 'ro', label='P1 0.5 P2 Nash', color = 'black')

#p2 0.5 p1 nash
x_2 = array1[A_x - 2]
y_2 = 0.5
ax.plot(x_2, y_2, 'ro', label='P2 0.5 P1 Nash', color = 'orange')


# Add labels and title
ax.set_xlabel(r'Probability of Player 1 choosing n-1 (instead of n)')
ax.set_ylabel(r'Probability of Player 2 choosing C (instead of L)')
ax.set_title('Expected Payoff')
ax.legend()

# Show the plot
plt.show()
