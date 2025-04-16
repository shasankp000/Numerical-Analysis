import numpy as np
import matplotlib.pyplot as plt

# Define the system via its iterative formulas:
# Given:
#   x + y - z = 7   -->  x = 7 - y + z
#   x - y + 2z = 3   -->  y = x + 2*z - 3
#   2x + y + z = 9   -->  z = 9 - 2*x - y
#
# The Gauss-Seidel update formulas are:
#   x_(k+1) = 7 - y_k + z_k
#   y_(k+1) = x_(k+1) + 2*z_k - 3
#   z_(k+1) = 9 - 2*x_(k+1) - y_(k+1)

# Choose initial guess
x0, y0, z0 = 0.0, 0.0, 0.0

# Number of iterations
num_iters = 5

# Lists to store iterations
x_vals = [x0]
y_vals = [y0]
z_vals = [z0]

# Current estimates
x_curr, y_curr, z_curr = x0, y0, z0

# Perform Gauss-Seidel iterations
for k in range(num_iters):
    # Update x using old y and z
    x_next = 7 - y_curr + z_curr
    # Update y using the newly updated x and old z
    y_next = x_next + 2*z_curr - 3
    # Update z using the new x and y
    z_next = 9 - 2*x_next - y_next
    
    # Append new values
    x_vals.append(x_next)
    y_vals.append(y_next)
    z_vals.append(z_next)
    
    # Update current values for the next iteration
    x_curr, y_curr, z_curr = x_next, y_next, z_next

# Prepare iteration numbers for x-axis
iterations = np.arange(num_iters + 1)

# Plot the values
plt.figure(figsize=(10, 6))
plt.plot(iterations, x_vals, marker='o', label='x')
plt.plot(iterations, y_vals, marker='s', label='y')
plt.plot(iterations, z_vals, marker='^', label='z')

plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Gauss-Seidel Iterations for the System')
plt.legend()
plt.grid(True)
plt.show()
