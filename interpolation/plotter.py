import matplotlib.pyplot as plt
import numpy as np
from lagrange_interpolation import LagrangeInterpolation
from newtons_interpolation import DividedDifferenceInterpolation

# Your data set
data_set = {
    5: 12,
    6: 13,
    9: 14,
    11: 16
}

# Points for plotting
x_points = np.linspace(min(data_set.keys()), max(data_set.keys()), 100)

# Initialize both interpolation objects
newton = DividedDifferenceInterpolation(data_set, 0, len(data_set))
newton.build_difference_table()

lagrange = LagrangeInterpolation(data_set, 0)

# Calculate interpolated y-values
newton_y = []
lagrange_y = []

for x in x_points:
    newton.x = x
    lagrange.x = x
    newton_y.append(newton.interpolate())
    lagrange_y.append(lagrange.interpolate())

# Original data points
plt.scatter(data_set.keys(), data_set.values(), color='red', label='Data Points')

# Newton's interpolated curve
plt.plot(x_points, newton_y, label="Newton's Interpolation", linestyle='--')

# Lagrange's interpolated curve
plt.plot(x_points, lagrange_y, label="Lagrange's Interpolation", linestyle='-.')

plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interpolation Comparison: Newton vs Lagrange')
plt.grid(True)
plt.show()
