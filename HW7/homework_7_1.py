from random import randint




class Matrix:

    # def __init__(self,input_data):
    #     self.input_data = input_data

    def __init__(self, initial_number, end_number, column_number, string_number):
        self.matrix = [[randint(initial_number, end_number) for i in range(column_number)] for x in
                       range(string_number)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):

        matrix_sum = [list(map(lambda x, y: x + y, el_1, el_2)) for el_1, el_2 in zip(self.matrix, other)]
        return matrix_sum


matrix_1 = Matrix(0, 9, 2, 2)
matrix_2 = Matrix(0, 9, 2, 2)
matrix_hand = [[1,2],[1,2]]

# print(matrix_1 + matrix_2)
print(matrix_1 + matrix_hand)