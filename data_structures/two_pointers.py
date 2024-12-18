# INFO: Problem is to find two sum: all pairs in a sorted array that sum up to a given target

def find_pairs_with_sum(arr, target):
    left, right = 0, len(arr)-1
    pairs = []

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -=1
        elif curr_sum < target:
            left+=1
        else:
            right-=1

    return pairs

def test_two_pointer():
    arr = [1,2,3,4,6,8,9]
    target = 10
    print("Two pointer result:", find_pairs_with_sum(arr, target))

if __name__ == '__main__':
    test_two_pointer()