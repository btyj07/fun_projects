'''Mean-Variance-Standard Deviation Calculator

Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

The returned dictionary should follow this format:
{
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standard deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
}

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.
'''

import numpy as np
import statistics

def calculate(arr):
    if len(arr) != 9: # only accepts 9 digit array
        raise ValueError("List must contain nine numbers.")
    
    else:
        reshaped = np.array(arr).reshape(3, 3)
        print(reshaped)

        mean_axis1 = reshaped.mean(axis=0).tolist()
        mean_axis2 = reshaped.mean(axis=1).tolist()
        flattened_mean = reshaped.mean()

        variance_axis1 = reshaped.var(axis=0).tolist()
        variance_axis2 = reshaped.var(axis=1).tolist()
        variance = reshaped.var()




        return {'mean': [mean_axis1, mean_axis2, flattened_mean],
                'variance': [variance_axis1, variance_axis2, variance],
                # 'standard deviation': [axis1, axis2, flattened],
                # 'max': [axis1, axis2, flattened],
                # 'min': [axis1, axis2, flattened],
                # 'sum': [axis1, axis2, flattened]
                }




test_array = [0,1,2,3,4,5,6,7,8]

if __name__ == "__main__":
    print(calculate(test_array))