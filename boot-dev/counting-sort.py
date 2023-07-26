import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    result = []
        
    for i in range(0, 100):
        result.append(0)
        
    for elem in arr:
        result[elem] += 1
    
    #print(len(result))
    return result

an_arr = [89, 37, 29, 73, 82, 58, 45, 84, 17, 88,46, 69, 60 ,20, 24 ,34, 49 ,52, 80, 43 ,72]

countingSort(an_arr)