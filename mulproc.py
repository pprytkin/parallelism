import random
from multiprocessing import Process, Pool

def generation(i):
    #Генерация рандомных матриц
    n = random.randint(2, 5)
    ls1 = [[random.randint(1,10) for i in range(n)] for j in range(n)]
    ls2 = [[random.randint(1,10) for i in range(n)] for j in range(n)]
    return ls1, ls2


def element(*args):
    #Перемножение  элементов и запись в промежуточный файл (prom.txt)
    i, j = args[0] #индекс элемента
    A = args[1] #Матрица 1
    B = args[2] #Матрица 2
    res = 0
    f = open("prom.txt", "a")
    
    for k in range(len(A[i])): #Перемножение элементов
        res += int(A[i][k]) * int(B[k][j])  
    f.write(str(res) + "\n") #Запись в промежуточный файл
    f.close()

    return res

def write_matrix(f, C, ln):
    #Запись матрицы в файл
    s = ""
    for i in range(ln):
        s = ""
        for j in range(ln):
                s += str(C[i+j]) + " "
        f.write(s + "\n")
    f.write("\n\n")

def start():
    # Генерируем матрицы
    with Pool(5) as p:
        mls = (p.map(generation, range(5)))
        print(mls)

        # Производим вычисления
        for i in mls:
            ln = len(i[0])
            with Pool(ln) as p1:
                mtrx3 = (p1.starmap(element, [((j,k), i[0], i[1]) for j in range(ln) for k in range(ln) ] ))
        # Записываем перемноженную матрицу в файл (matrix_3.txt)
            f = open("matrix_3.txt", "a")    
            write_matrix(f, mtrx3, ln)
            f.close()

if __name__ == '__main__':
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    start()
