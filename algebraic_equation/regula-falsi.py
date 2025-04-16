from collections import defaultdict

# write the equation.

# The function f(x) = x^3 - x - 1 # adjust as needed

## default starting values.

possible_roots = []

def f(x) -> float|int:
    return x**3 - x - 1 # adjust as needed

data_set = defaultdict(list) # initialize a dictionary of arrays


def interpolate(a: float | int , b: float | int) -> float | int:
    c = ((a * f(b)) - (b * f(a)))/(f(b) - f(a))
    return c

# The regula falsi method 

def regula_falsi(a: float | int , b: float | int , max_iter:int) -> float | int:
    if (a and b <= 0):
        print("Error! Both the intervals cannot be of the same sign!")
        return ValueError
    
    for i in range(max_iter):
        # run for a set amount of iterations
        c = interpolate(a, b)

        array = [i+1, a, b, c, f(c)]

        data_set[i].append(array)

        if (f(a) * f(c) < 0):
            b = c
        else:
            a = c



regula_falsi(1, 2, 10)

for j in range(len(data_set)):
    print(data_set[j])

for k in range(len(data_set)):
    if abs(data_set[k][0][4]) <= 0.003:
        possible_roots.append(data_set[k][0][3])

    
print("The most precise real root as per the set number of iterations for this equation is: ", possible_roots[-1])


