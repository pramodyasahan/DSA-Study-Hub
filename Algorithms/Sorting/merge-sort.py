from typing import List


def merge_sorted_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    """
    Merges two sorted arrays into a single sorted array.

    :param arr1: First sorted array.
    :param arr2: Second sorted array.
    :return: A merged sorted array.
    """
    i, j = 0, 0
    m, n = len(arr1), len(arr2)
    merged_arr = []

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    # Append remaining elements (if any)
    merged_arr += arr1[i:]
    merged_arr += arr2[j:]

    return merged_arr


# Example usage
arr1 = [1, 3, 5, 7, 9, 11]
arr2 = [2, 4, 6, 8, 10, 12]

sorted_arr = merge_sorted_arrays(arr1, arr2)
print(sorted_arr)
