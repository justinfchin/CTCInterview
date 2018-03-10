def insertionSort(arr):
    """
    Args:
        arr : array
    Returns:
        sorted array
    """

    for i in range(1,len(arr)): # iter through each item without checking the first element
        target = arr[i]
        j = i-1
        while j >= 0 and target <= arr[j]: # check everything to the left
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = target

    return arr

if __name__ == '__main__':
    print(insertionSort([2,4,3,1]))
