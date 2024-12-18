# INFO: The problem is to find the maximum sum of any subarray of size k.

def max_sum_subarray_k(arr, k):
    if len(arr) < k:
        raise ValueError("Array size must be greater than or equal to k")

    max_sum = curr_sum = sum(arr[:k]) #Initial window sum
    for i in range(k, len(arr)):
        curr_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, curr_sum)

    return max_sum


def test_sliding_window():
    arr = [2,1,5,1,3,2]
    k = 3
    print("Sliding window result:", max_sum_subarray_k(arr, k))


if __name__ == "__main__":
    test_sliding_window()
