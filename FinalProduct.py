import time
import random
from NormalSort import normalSort
from MergeSort import mergeSort
from QuickSort import quickSort

nums = []

for i in range(1, 10000):
    tolist = random.randint(1, 10000)
    nums.append(tolist)

starttime = time.time()
normalSort(nums)
endtime = time.time()
print('normalSort', endtime - starttime)

starttime = time.time()
mergeSort(nums)
endtime = time.time()
print('mergeSort', endtime - starttime)

starttime = time.time()
quickSort(nums)
endtime = time.time()
print('quickSort', endtime - starttime)
