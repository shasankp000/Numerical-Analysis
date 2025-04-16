# Newton's forward and backward difference interpolation for equal intervals.

from typing import Dict, List

# data set of population growth over the years
data_set = {
    1891: 46, 
    1901: 66, 
    1911: 81, 
    1921: 93, 
    1931: 101
}


# data set of unequal intervals.
data_set1 = {
    5:12,
    6:13,
    9:14,
    11:16
}


class Interpolation():
    def __init__(self, data_set: Dict, max_iter:int, step_size: int, start_point: int|float, end_point: int|float):
        self.data_set = data_set
        self.max_iter = max_iter
        self.step_size = step_size
        self.keys_list = list(data_set.keys())
        self.start_point = start_point
        self.end_point = end_point
        self.difference_table = []

    def factorial(self, x) -> int:

        if (x == 1 or x==1):
            return 1

        fact = x
        x-=1
        while True:
            fact *= x
            x-=1

            if (x == 0):
                break
        
        return fact

    def get_f_values_from_dataset(self) -> List[int]:
        f_values = []
        
        for i in range(len(self.keys_list)):
            f_values.append(self.data_set.get(self.keys_list[i]))

        return f_values    


    def delta_f(self , f_values: list[int|float]) -> List[int]:

        del_f_values = []
  
        for j in range(len(f_values) - 1):
            del_f_values.append((f_values[j+1] - f_values[j]))

        return del_f_values
    

    def get_forward_p(self) -> float|int:
        return ((self.start_point - self.keys_list[0])/self.step_size)

    def get_backward_p(self) -> float|int:
        return ((self.end_point - self.keys_list[-1])/self.step_size)
   
    
    def build_difference_table(self) -> List[int|float]:
        table = []

        del_f = []

        table.append(self.get_f_values_from_dataset()) # first column
        
        for k in range(self.max_iter):
            del_f = self.delta_f(table[k])
            table.append(del_f)

        self.difference_table = table # assign the table.

        return table
    
    def forward_interpolate(self) -> int|float:

        self.build_difference_table()

        p_x = 0

        p = self.get_forward_p()
        
        p_x += self.difference_table[0][0] # f(x0)

        multiplier = 1

        for i in range(1, self.max_iter):
            multiplier *= (p - i + 1)  # Compute p*(p-1)*... for the term
            term = (multiplier / self.factorial(i)) * self.difference_table[i][0]
            p_x += term


        return p_x

    def backward_interpolate(self) -> int|float:
        self.build_difference_table()        

        p_x = 0

        p = self.get_backward_p()

        p_x += self.difference_table[0][-1] # f(xn)

        multiplier = 1

        for i in range(1, self.max_iter):
            multiplier *= (p + i - 1)  # Compute p*(p+1)*... for the term
            term = (multiplier / self.factorial(i)) * self.difference_table[i][-1]
            p_x += term

        return p_x
    

##############################################################################################################################################################################################
# Newton's divided difference interpolation for unequal intervals


class DividedDifferenceInterpolation():
    def __init__(self, data_set: dict, x: int|float, max_iter:int):
        self.data_set = data_set
        self.keys_list = list(data_set.keys())
        self.start_point = x
        self.max_iter = max_iter
        self.difference_table = []
        self.delta = 1
        self.x = x

    def get_f_values(self) -> list:
        f_values = []
        
        for i in range(len(self.keys_list)):
            f_values.append(self.data_set.get(self.keys_list[i]))

        return f_values  

    def delta_f(self, f_values: List[float], level: int) -> List[float]:
        """
        Computes the divided differences for the given f_values at a particular level.
        The denominator is determined by the x difference: (x[j+level] - x[j]).
        """
        del_f_values = []
        for j in range(len(f_values) - 1):
            # Calculate the denominator using the keys_list which should be sorted
            denominator = self.keys_list[j + level] - self.keys_list[j]

            del_f_values.append(((f_values[j+1] - f_values[j]) / denominator))
            
        return del_f_values

    def build_difference_table(self):
        table = []
        table.append(self.get_f_values()) # f(x) column

        # Use level starting from 1 up to max_iter - 1.
        for level in range(1, self.max_iter):
            previous_column = table[level-1]
            current_column = self.delta_f(previous_column, level)
            table.append(current_column)

        self.difference_table = table

        for i, column in enumerate(self.difference_table):
            print(f"Level {i}: {column}")


    def interpolate(self) -> int|float:
        self.build_difference_table()
        
        p_x = 0
        p_x += self.difference_table[0][0]

        multiplier = 1

        # For divided difference interpolation, the product for term i is (x - x0)(x - x1)...(x - x(i-1))
        for i in range(1, self.max_iter):
            multiplier *= (self.x - self.keys_list[i-1]) # (x-x0), (x-x1), (x-x2)....
            term = multiplier * self.difference_table[i][0]
            p_x += term

        return p_x


fwd_interpolation = Interpolation(data_set, 4, 10, 1895, 1925) # we are asked to find the population between these years
print(fwd_interpolation.get_forward_p())
print(fwd_interpolation.get_backward_p())
print(f"Forward Interpolation Result at x=1895: {fwd_interpolation.forward_interpolate():.2f}")
print(f"Backward Interpolation Result at x=1925: {fwd_interpolation.backward_interpolate():.2f}")
difference_table = fwd_interpolation.difference_table

for i, column in enumerate(difference_table):
    print(f"Level {i}: {column}")

print()

div_interpolation = DividedDifferenceInterpolation(data_set1, 10, 4)
print(f"Divided difference result at x=10: {div_interpolation.interpolate():.3f}")