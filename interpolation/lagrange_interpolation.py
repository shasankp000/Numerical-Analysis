# Lagrange's interpolation method for unequal intervals.

# data set of unequal intervals.
data_set1 = {
    5:12,
    6:13,
    9:14,
    11:16
}


class LagrangeInterpolation():
    def __init__(self, data_set:dict ,x:int|float):
        self.data_set = data_set
        self.x = x
        self.keys_list = list(self.data_set.keys())
        self.f_values = [self.data_set[key] for key in self.keys_list] # one-liner for loop


    def interpolate(self) -> int|float:

        l = 0

        for i in range(len(self.keys_list)):

            temp_list = self.keys_list.copy() # temp_list gets reinitialized back to the keys list, actually copies the list instead of passing a reference to the keys list's memory location.

            temp_element = self.keys_list[i] # store the element to be removed
            temp_list.pop(i) # remove the currently selected element from the list.
            
            # numerator and denominator will always be initialized to 1, each iteration

            numerator = 1  
            denominator = 1

            for j in range(len(temp_list)):
                # build the numerator and denominator terms
                numerator *= (self.x - temp_list[j])
                denominator *= (temp_element - temp_list[j])

            l += ((numerator/denominator) * self.f_values[i]) # multiply the fraction of numerator upon denominator by the corresponding f(x) value of the removed element

        return l
    

lg_interpolation = LagrangeInterpolation(data_set1, 10)
print(f"The value at x = {10} is: {lg_interpolation.interpolate():.3f}")