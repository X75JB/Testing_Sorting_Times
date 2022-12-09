def mergeSort(nums: list[float]) -> list[float]:
    if len(nums) == 1:
        return nums
    elif len(nums) > 1:
        half = len(nums) // 2
        splitOne = nums[0:half]
        splitTwo = nums[half:len(nums)]
        sortedOne = mergeSort(splitOne)
        sortedTwo = mergeSort(splitTwo)
        finishedSort = merge(sortedOne, sortedTwo)
        return finishedSort

def merge(splitOne: list[float], splitTwo: list[float]) -> list[float]:
    counterOne = 0
    counterTwo = 0
    finalMerge = []

    sizeOne = len(splitOne)
    sizeTwo = len(splitTwo)

    while counterOne < sizeOne and counterTwo < sizeTwo:
        if splitOne[counterOne] <= splitTwo[counterTwo]:
            finalMerge.append(splitOne[counterOne])
            counterOne = counterOne + 1
        elif splitOne[counterOne] > splitTwo[counterTwo]:
            finalMerge.append(splitTwo[counterTwo])
            counterTwo = counterTwo + 1
    if counterOne >= sizeOne:
        finalMerge = finalMerge + splitTwo[counterTwo:sizeTwo]
    else:
        finalMerge = finalMerge + splitOne[counterOne:sizeOne]

    return finalMerge
