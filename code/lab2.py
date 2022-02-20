def make_set(matrix, size):

    set_view = []

    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1:
                set_view.append((i + 1, j + 1))
    return sorted(set_view)


def matrix_set_view(matrix_set, flag=None):
    if not flag:
        print('Исходное отношение: {', end='')
        print(*matrix_set, sep=', ', end='}\n')
    else:
        print('{', end='')
        print(*matrix_set, sep=', ', end='; ')


def factor_set(matrix, size):
    return [{j + 1 for j, value in enumerate(matrix[i]) if value == 1} for i in range(size)]


def make_equivalent_closure(copy, size):
    list_for_equivalent_closure = set()
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                copy[j][i] = 1
                list_for_equivalent_closure.add((j + 1, i + 1))
        if matrix[i][i] == 0:
            copy[i][i] = 1
            list_for_equivalent_closure.add((i + 1, i + 1))

    for _ in range(size):
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if copy[k][i] == copy[i][j] == 1 and copy[k][j] == 0:
                        copy[k][j] = 1
                        list_for_equivalent_closure.add((k + 1, j + 1))

    return sorted(list_for_equivalent_closure), copy


def is_transitive(matrix, size):

    for k in range(size):
        for i in range(size):
            for j in range(size):
                if matrix[k][i] == matrix[i][j] == 1 and matrix[k][j] == 0:
                    return False
    return True


def is_symmetric_or_antisymmetric(matrix, size):

    flag_symmetric = True
    flag_antisymmetric = True

    for i in range(size):
        for j in range(size):
            if not matrix[i][j] == matrix[j][i]:
                flag_symmetric = False
            elif matrix[i][j] == matrix[j][i] and not i == j:
                flag_antisymmetric = False
            elif not flag_symmetric and not flag_antisymmetric:
                return False, False

    return flag_symmetric, flag_antisymmetric


def is_reflexive_or_anti_reflexive(matrix, size):

    flag_reflexive = True
    flag_anti_reflexive = True

    for i in range(size):
        if matrix[i][i] == 0:
            flag_reflexive = False
        elif matrix[i][i] == 1:
            flag_anti_reflexive = False
        if not flag_reflexive and not flag_anti_reflexive:
            return False, False

    return flag_reflexive, flag_anti_reflexive


def get_data():
    n = int(input())
    m = [[int(elem) for elem in input().split()] for _ in range(n)]
    m_set = [(i + 1, j + 1) for i in range(n) for j in range(n) if m[i][j] == 1]
    return m, sorted(m_set), n


matrix, matrix_set, size = get_data()

copy = matrix
ls, mt = make_equivalent_closure(copy, size)

print('Матрица эквивалентного замыкания бинарного отношения:')
for i in range(len(mt)):
    print(*mt[i])
print('\n')
print('Фактор-множество бинарного отношения:')
print(factor_set(mt, size))
'''
Примеры входных данных:

4
0 1 1 0
1 1 1 0
0 1 1 0
0 0 0 1

4
0 1 0 0
0 0 0 0
0 0 0 1
0 1 0 0

3 
0 1 0
0 0 1
1 0 0

5
1 0 1 1 0
0 1 0 1 0
1 0 1 1 0
1 1 1 1 0
0 0 0 0 1

4
1 1 0 1
0 1 1 0 
0 0 1 1
0 0 0 1

4
0 0 1 0 
1 0 0 1
0 0 0 0
0 1 0 0
'''