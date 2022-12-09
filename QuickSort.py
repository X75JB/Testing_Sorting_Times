def quickSort(nums: list[float]) -> list[float]:
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return nums
    elif len(nums) > 1:
        left_list, pivot, right_list = partition(nums)
        leftSorted = quickSort(left_list)
        rightSorted = quickSort(right_list)
        return leftSorted + [pivot] + rightSorted


def partition(nums: list[float]):
    pivot = nums[0]
    left_list = []
    right_list = []

    for i in range(1, len(nums)):
        if nums[i] <= pivot:
            left_list.append(nums[i])
        else:
            right_list.append(nums[i])

    return left_list, pivot, right_list
