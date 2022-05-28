class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return str('\n'.join(str(i) for i in self.matrix_list))

    def __add__(self, other):
       new_list = [[0 for j in range(len(self.matrix_list[0]))] for i in range(len(self.matrix_list))] #создаём пустую матрицу нужной размерности
       for i in range(len(self.matrix_list)):      #проходим по столбцам
          for j in range(len(self.matrix_list[0])):  #проходим по строкам
             new_list[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j] #cкладываем
       return str('\n'.join(str(i) for i in new_list))


mc_1 = Matrix([[10, 20, 56], [30, 40, 56]])
mc_2 = Matrix([[50, 60, 56], [70, 80, 56]])
print(mc_1)
print(mc_2)
print(mc_1 + mc_2)
