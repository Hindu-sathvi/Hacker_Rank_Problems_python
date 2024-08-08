import numpy as np
input_str = input()
input_list = list(map(int, input_str.split()))
array = np.array(input_list).reshape(3, 3)
print(array)
