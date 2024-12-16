from transpose_matrix import transpose_matrix_

def rotate_matrix(matrix, angle, direction=None):
    if angle == 90 and direction == "clockwise":
        transposed_matrix = transpose_matrix_(matrix)
        for row in transpose_matrix_(matrix):
            row.reverse()
        return transposed_matrix
    if angle == 90 and direction == "anticlockwise":
        for row in matrix:
            row.reverse()
        return transpose_matrix_(matrix)
    if angle == 180:
        return [row[::-1] for row in matrix[::-1]]


def test_rotations():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(rotate_matrix(matrix, 90, "clockwise"))
    print(rotate_matrix(matrix, 90, "anticlockwise"))
    print(rotate_matrix(matrix, 180))

if __name__ == "__main__":
    test_rotations()





