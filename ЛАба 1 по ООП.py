# С1 = 3132 % 2 = 0, C =  3132 % 3 = 0, C3 = 3132 % 5 = 2
class Main:
    def __init__(self):
        self.S = 0

    def calculate_sum(self, a, b, n, m, C):
        if a + C != 0:
            for i in range(a, n + 1):
                for j in range(b, m + 1):
                    denominator = 1 + 0  # This is effectively 1
                    if denominator != 0:
                        self.S += (i % j) / denominator
                    else:
                        print("Error: Division by zero!")
                        return
            print(self.S)
        else:
            print("Error: a + C == 0")

if __name__ == "__main__":
    main = Main()
    a = 3
    b = 2
    n = 5
    m = 2
    C = 0
    main.calculate_sum(a, b, n, m, C)

