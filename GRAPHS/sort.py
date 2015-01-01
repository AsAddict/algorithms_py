import util
import time
#############################################################################
#                              SelectSort                                   #
#############################################################################


def insert_sort(array):
    n = len(array)
    for i in range(n-1):
        j = i + 1
        while(j >= 1):
            if array[j] < array[j-1]:
                util.swap(array, j, j-1)
            j = j - 1

#############################################################################
#                              InsertSort                                   #
#############################################################################


def select_sort(array):
    n = len(array)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j
        util.swap(array, i, min)

#############################################################################
#                          MergeSort Recusive                               #
#############################################################################


def merge(array, low_bound, mid, high_bound):
    if low_bound == high_bound:
        return
    if low_bound > high_bound:
        return
    aux[low_bound:high_bound+1] = array[low_bound:high_bound+1]
    i, j = low_bound, mid+1
    for m in range(low_bound, high_bound+1):
        if i >= mid+1:
            array[m] = aux[j]
            j += 1
        elif j > high_bound:
            array[m] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            array[m] = aux[i]
            i += 1
        else:
            array[m] = aux[j]
            j += 1

aux = list()


def merge_sort(array):
    merge_sort_impl(array, 0, len(array)-1)


def merge_sort_impl(array, low_bound, high_bound):
    if low_bound == high_bound:
        return
    if low_bound > high_bound:
        return
    mid = low_bound + (high_bound - low_bound)/2
    merge_sort_impl(array, low_bound, mid)
    merge_sort_impl(array, mid+1, high_bound)
    merge(array, low_bound, mid, high_bound)


#############################################################################
#                          MergeSort BottomUp                               #
#############################################################################

a = time.clock()
with open("tiny.txt") as file:
    strs = list(file)
    insert_sort(strs)
    print(strs)
b = time.clock()
print(a-b)
