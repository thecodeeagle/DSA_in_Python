# INFO : Find the largest sum of a contiguous subarray

def max_subarray_sum(arr):
    max_sum = curr_sum = arr[0]

    curr_sub_array = []
    curr_sub_array.append(curr_sum)
    max_sub_array = curr_sub_array

    for num in arr[1:]:
        if curr_sum+num > num:
            curr_sub_array.append(num)
            curr_sum = curr_sum+num
        else:
            curr_sub_array = [num]
            curr_sum = num
        if max_sum < curr_sum:
            max_sum = curr_sum
            max_sub_array = curr_sub_array[:] # copy only the current version of curr_sub_array, and not subsequent modifications

    return max_sub_array, max_sum

def test_kadane():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Kadane's Algorithm Result:", max_subarray_sum(arr))

if __name__ == "__main__":
    test_kadane()

