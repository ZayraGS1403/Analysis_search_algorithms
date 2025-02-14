"""
This algorithm is the simplest one, it just iterates
over the array and compares each element with the target.
The time complexity of this algorithm is O(n) because
it has to iterate over all the elements of the array.
@param arr: The array where the algorithm will search the target.
@param target: The element that the algorithm will search in the array.
@return: True if the target is in the array, False otherwise.

"""


def lineal_search(arr, target):
    for i in range(len(arr)):  # O(n)
        if arr[i] == target:  # O(1)
            return True  # O(1)
    return False  # O(1)


# O(lineal_search) = O(n) * O(1) * O(1) + O(1)
# O(lineal_search) = O(n)


"""
    This algorithm is a little bit more complex than the previous one.
    It uses the 'in' operator to check if the target
    is in the array. The time complexity of this algorithm is O(n)
    because the 'in' operator has to iterate over all the
    elements of the array.
    @param arr: The array where the algorithm will search the target.
    @param target: The element that the algorithm will search in the array.
    @return: True if the target is in the array, False otherwise.
"""


def search_in(arr, target):
    if target in arr:  # O(n) en el peor caso
        return True  # O(1)
    else:
        return False  # O(1)


# O(search_in) = O(n) * O(1) + O(1)
# O(search_in) = O(n)


"""
    It uses the binary search algorithm to find the target in the array.
    The time complexity of this algorithm is O(log n) because it divides
    the problem size by half in each iteration.
    The array must be sorted.
    @param arr: The array where the algorithm will search the target.
    @param target: The element that the algorithm will search in the array.
    @return: True if the target is in the array, False otherwise.
"""


def binary_search(arr, target):
    left = 0  # O(1)
    rigth = len(arr) - 1  # O(1)

    while (
        left <= rigth
    ):  # It runs ( O(log n)) times because, in each iteration, the problem size is reduced by half.
        mid = left + (rigth - left) // 2  # O(1)

        if arr[mid] == target:  # O(1)
            return True  # O(1)

        elif arr[mid] < target:  # O(1)
            left = mid + 1  # O(1)

        else:
            rigth = mid - 1  # O(1)
    return False  # O(1)


# o(binary_search) = O(log n) * O(6) + O(2)
# o(binary_search) = O(log n)

"""
    It uses the ternary search algorithm to find the target in the array.
    The time complexity of this algorithm is O(log 3 n) because it divides
    the problem size by three in each iteration.
    The array must be sorted.
    @param arr: The array where the algorithm will search the target.
    @param target: The element that the algorithm will search in the array.
    @return: True if the target is in the array, False otherwise.
"""


def ternary_search(arr, target):
    if len(arr) == 0:  # O(1)
        return False  # O(1)
    else:
        mid1 = len(arr) // 3  # O(1)
        mid2 = mid1 * 2  # O(1)

        if arr[mid1] == target or arr[mid2] == target:  # O(1)
            return True  # O(1)

        elif arr[mid1] > target:
            return ternary_search(arr[:mid1], target)  # O(T(n/3))

        elif arr[mid2] < target:
            return ternary_search(arr[mid2 + 1:], target)  # O(T(n/3))

        else:
            return ternary_search(arr[mid1 + 1: mid2], target)  # O(T(n/3))


# O(ternary_search) = o(log 3 n)
