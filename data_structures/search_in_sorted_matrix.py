
def search_in_sorted_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])-1
    row, col = 0, cols-1

    while row< rows and col>=0:
        if matrix[row][col] == target:
            return row, col
        elif matrix[row][col]>target:
            col-=1
        else:
             row +=1
    return -1, -1

def test():
    matrix = [[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50]]
    print("Search (29):", search_in_sorted_matrix(matrix, 29))


if __name__ == "__main__":
    test()