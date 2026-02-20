def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)
    swap(arr, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort_helper(arr, left, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, right)
    return arr

def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    myarray = [4,6,1,7,3,2,5]
    # pivot_index = pivot(my_array, 0, len(my_array) - 1)
    # print(pivot_index)
    # print(my_array)
    print(quick_sort(my_array))