
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

def test_transpose_matrix():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print("Transpose:", transpose_matrix(matrix))

test_transpose_matrix()