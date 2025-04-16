from collections import defaultdict
import sympy as smp
import numpy as np

# given equation
# 2(x-3) = log_10 (x) or 2(x-3) - log_10(x) = 0 or 2x - 6 - log_10(x) = 0 # simplified the equation for the code to use cheaper operations.


x = smp.symbols("x")
eqn = 2*x - 6 - smp.log(x, 10) # set the equation as needed

f_numeric = smp.lambdify(x, eqn)
eqn_derivative = smp.diff(eqn, x)
f_deriv_numeric = smp.lambdify(x, eqn_derivative) 


data_set = defaultdict(list) # default dictionary of arrays



def f(x) -> float|int:
    return f_numeric(x)

def fprime(x) -> float|int:
    return f_deriv_numeric(x)


def newton_raphson(x_n: int, n: int):
    for i in range(n): # run for n iterations
        x_n1 = x_n - (f(x_n) / fprime(x_n))
        array = [i, x_n, x_n1]
        data_set[i].append(array)

        x_n = x_n1 # update the value



newton_raphson(3.5, 10)

for k in range(len(data_set)):
    print(data_set[k])


print("The most precise real root for this equation is: ", data_set.get(list(data_set.keys())[-1])[0][2])
