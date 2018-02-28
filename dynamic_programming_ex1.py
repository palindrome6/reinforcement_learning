import numpy as np

matrix = -1*np.zeros((4, 4))

def update_matrix(old_matrix, iterations):
    new_matrix = np.array(old_matrix)
    print(old_matrix)
    for k in range(iterations):
        for i in range(4):
            for j in range(4):

                if  (i == 0 and j== 0) or (i == 3 and j == 3):
                    continue
                elif i == 0 and j != 3:
                    new_matrix[i][j] = (-1+old_matrix[i][j])*0.25 + \
                    (-1+old_matrix[i][j-1])*0.25 + (-1+old_matrix[i][j+1])*0.25 + (-1+old_matrix[i+1][j])*0.25

                elif i == 0 and j == 3:
                    new_matrix[i][j] = (-1+old_matrix[i][j])*0.50 + \
                    (-1+old_matrix[i][j-1])*0.25 + (-1+old_matrix[i+1][j])*0.25

                elif j == 0 and i != 3:
                    new_matrix[i][j] = (-1+old_matrix[i][j])*0.25 + (-1+old_matrix[i-1][j])*0.25 + \
                    (-1+old_matrix[i][j+1])*0.25 + (-1+old_matrix[i+1][j])*0.25

                elif j == 3:
                    new_matrix[i][j] = (-1+old_matrix[i][j])*0.25 + (-1+old_matrix[i-1][j])*0.25 + \
                    (-1+old_matrix[i][j-1])*0.25 + (-1+old_matrix[i+1][j])*0.25

                elif j == 0 and i == 3:
                    new_matrix[i][j] = (-1+old_matrix[i][j])*0.50 + (-1+old_matrix[i-1][j])*0.25 + \
                    (-1+old_matrix[i][j+1])*0.25

                elif i == 3:
                    new_matrix[i][j] = (-1+old_matrix[i][j])*0.25 + (-1+old_matrix[i][j-j])*0.25 + \
                    (-1+old_matrix[i-1][j])*0.25 + (-1+old_matrix[i][j+1])*0.25

                else:
                    new_matrix[i][j] = (-1+old_matrix[i-1][j])*0.25 + (-1+old_matrix[i+1][j])*0.25 + \
                    (-1+old_matrix[i][j-1])*0.25 + (-1+old_matrix[i][j+1])*0.25
        old_matrix = np.array(new_matrix)
    return new_matrix

print(update_matrix(matrix,100))
