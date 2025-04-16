# default euler's method, computationally expensive due to small step-size requirements.

import sympy as smp
from collections import defaultdict

# given equation 
# dy/dx = x + y # this is a differential equation, not an explicit equation

# formula for euler's method 
# y_{n+1} = y_n + h . f'(x_n, y_n) # if an explicit equation else just f(x_n, y_n)

output_table = defaultdict(list)

x, y = smp.symbols("x y") # using two symbols since we are dealing with an actual ODE.

eqn = x + y

f_numeric = smp.lambdify((x, y),  eqn)

# we only need to find out the derivative ourselves if we are dealing with an explicit function.

# eqn_derivative = smp.diff(eqn, x)
# f_diff_numeric = smp.lambdify(x, eqn_derivative)


def f(x, y) -> int|float:
   return (f_numeric(x, y)) 

# def fprime(x) -> int|float:
#     return (f_diff_numeric(x))

def get_step_size(x_final:int, x:int, n_total:int) -> int|float:
    print((x_final - x) / n_total)
    return ((x_final - x) / n_total)


def find_soln(n_total: int, x_final:int|float, x=1, y=1):
    h = get_step_size(x_final=x_final, x=x, n_total=n_total)

    y_n = y
    x_n = x
    actual_value = f(x_n, y_n)

    output_table[0].append([0, x_n, y_n, actual_value])

    x_n+=h # increment the value by the step size.

    for n in range(1, n_total+1): # Starts at n=1, find n_total+1, stop at n_total+1. For example if n_total=5, loop will run till 1, 2, 3, 4, 5 (since range=6)
        y_nplus1 = y_n + (h * f(x_n, y_n))

        y_n = y_nplus1

        actual_value = f(x_n, y_n)

        output_table[n].append([n, x_n, y_n, actual_value])

        x_n+=h # increment the value of x_n by adding the step size.

    

find_soln(5, 0.1, 0)

for i in range(len(output_table)):
    print(output_table[i])

target_x = 0.1

for key, value in output_table.items():
    for item in value:
        if item[1] == target_x:
            print(f"The value of y at x = {target_x} is: {output_table.get(key)[0][2]}")
            break
                