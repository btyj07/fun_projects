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

def calculate(arr) -> dict:
    if len(arr) != 9: # only accepts 9 digit array
        raise ValueError("List must contain nine numbers.")
    
    else:
        reshaped = np.array(arr).reshape(3, 3)
        print(reshaped)

        mean_axis1 = reshaped.mean(axis=0).tolist()
        mean_axis2 = reshaped.mean(axis=1).tolist()
        mean_flattened = reshaped.mean()

        variance_axis1 = reshaped.var(axis=0).tolist()
        variance_axis2 = reshaped.var(axis=1).tolist()
        variance_flattened = reshaped.var()

        std_dev_axis1 = reshaped.std(axis=0).tolist()
        std_dev_axis2 = reshaped.std(axis=1).tolist()
        std_dev_flattened = reshaped.std()

        max_axis1 = reshaped.max(axis=0).tolist()
        max_axis2 = reshaped.max(axis=1).tolist()
        max_flattened = reshaped.max
        
        min_axis1 = reshaped.min(axis=0).tolist()
        min_axis2 = reshaped.min(axis=1).tolist()
        min_flattened = reshaped.min()

        sum_axis1 = reshaped.sum(axis=0).tolist()
        sum_axis2 = reshaped.sum(axis=1).tolist()
        sum_flattened = reshaped.sum()

        return {'mean': [mean_axis1, mean_axis2, mean_flattened],
                'variance': [variance_axis1, variance_axis2, variance_flattened],
                'standard deviation': [std_dev_axis1, std_dev_axis2, std_dev_flattened],
                'max': [max_axis1, max_axis2, max_flattened],
                'min': [min_axis1, min_axis2, min_flattened],
                'sum': [sum_axis1, sum_axis2, sum_flattened]
                }


test_array = [0,1,2,3,4,5,6,7,8]

if __name__ == "__main__":
    print(calculate(test_array))