class Matrix:
    matrix1 = ""
    matrix2 = ""
    k = ""

    def Summ(self,matrix1,matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
        try:
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    result[i][j] = matrix1[i][j] + matrix2[i][j]
            for r in result:
                  print(r)
        except Exception:
            print("Не удалось сложить эти две матрицы! \n")
            task()

    def multi(self,matrix1,matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
        try:
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                  for k in range(len(matrix2)):
                          result[i][j] += matrix1[i][k] * matrix2[k][j]
            for r in result:
                  print(r)
        except Exception:
            print("Не удалось умножить эти две матрицы! \n")
            task()

    def multichislo(self,matrix1,k):
        self.matrix1 = matrix1
        self.k = k
        result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
        try:
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    result[i][j] += matrix1[i][j] * k
            for r in result:
                  print(r)
        except Exception:
            print("Не удалось умножить эту матрицу на число! \n")
            task()

    def transpose(self, matrix1):
        self.matrix1 = matrix1
        result = []
        n=len(matrix1)
        m=len(matrix1[0])
        try:
            for j in range(m):
                tmp=[]
                for i in range(n):
                    tmp=tmp+[matrix1[i][j]]
                result=result+[tmp]
            for r in result:
                  print(r)
        except Exception:
            print("Не удалось транспонировать эту матрицу! \n")
            task()
            
def Solution(matrix1,matrix2,k):
    matrixes = Matrix()
    print("Сумма двух матриц:")
    matrixes.Summ(matrix1,matrix2)
    print("Умножение двух матриц:")
    matrixes.multi(matrix1,matrix2)
    print("Умножение матрицы 1 на число {0}:".format(k))
    matrixes.multichislo(matrix1,k)
    print("Умножение матрицы 2 на число {0}:".format(k))
    matrixes.multichislo(matrix2,k)
    print("Транспонирование матрицы 1:")
    matrixes.transpose(matrix1)
    print("Транспонирование матрицы 2:")
    matrixes.transpose(matrix2)

def task():
    try:
        sh_matrix1=int(input("Введите количество строк 1 матрицы: "))
        v_matrix1=int(input("Введите количество столбцов 1 матрицы: "))
        matrix1 = [[0] * sh_matrix1 for i in range(v_matrix1)]
        sh_matrix2=int(input("Введите количество строк 2 матрицы: "))
        v_matrix2=int(input("Введите количество столбцов 2 матрицы: "))
        matrix2 = [[0] * sh_matrix2 for i in range(v_matrix2)]
        print("\nВведите 1 матрицу:")
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                matrix1[i][j] = int(input("Введите [{0}][{1}] элемент матрицы: ".format(i+1,j+1)))
        print("\nВведите 2 матрицу:")
        for i in range(len(matrix2)):
            for j in range(len(matrix2[0])):
                matrix2[i][j] = int(input("Введите [{0}][{1}] элемент матрицы: ".format(i+1,j+1)))
        k = int(input("Введите число: "))
        Solution(matrix1,matrix2,k)
    except Exception:
        print("Что-то пошло не так! :( ")
        task()
task()
