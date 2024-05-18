# C11 = 3132 % 11 = 8, C5 = 3132 % 5 = 2, C7 = int
class Laba2:
    def __init__(self, size1, size2, a):
        self.size1 = size1
        self.size2 = size2
        self.a = a
        self.matrix1 = []
        self.matrix2 = []

    def fill_matrices(self):
        for i in range(self.size1):
            row1 = []
            row2 = []
            for j in range(self.size2):
                value1 = i + j  # Значення для першої матриці
                value2 = value1 * self.a  # Значення для другої матриці
                row1.append(value1)
                row2.append(value2)
            self.matrix1.append(row1)
            self.matrix2.append(row2)

    def multiply_matrices(self):
        result_matrix = []
        for i in range(self.size1):
            row = []
            for j in range(self.size2):
                product = self.matrix1[i][j] * self.matrix2[i][j]
                row.append(product)
            result_matrix.append(row)
        return result_matrix

    def print_matrices(self):
        print("Перша матриця:")
        self.print_matrix(self.matrix1)
        print("\nДруга матриця:")
        self.print_matrix(self.matrix2)

    def print_matrix(self, matrix):
        for row in matrix:
            for value in row:
                print(f"{value:<4}", end="")
            print()

    def print_result_matrix(self, result_matrix):
        print("\nРезультат множення матриць:")
        self.print_matrix(result_matrix)

    def print_row_averages(self, result_matrix):
        print("\nСереднє значення елементів кожного рядка результуючої матриці:")
        for row in result_matrix:
            row_average = sum(row) // len(row)
            print(f"{row_average}", end=" ")
        print()


def main():
    size1 = 3
    size2 = 7
    a = 3

    lab = Laba2(size1, size2, a)
    lab.fill_matrices()
    result_matrix = lab.multiply_matrices()

    lab.print_matrices()
    lab.print_result_matrix(result_matrix)
    lab.print_row_averages(result_matrix)


if __name__ == "__main__":
    main()
