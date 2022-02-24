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


def print_factor(res_set, res_representatives, factor):

    print('Фактор-множество отношения: {' + str(res_set)[1:-1] + '}, где ', end='')

    for i, representative in enumerate(res_representatives):

        print(str(res_set[i]) + ' \u2208 '
              + f'\u03B5({representative})={list(map(lambda x: x[0], factor[i]))}', end='')

        if i < len(res_representatives) - 1:
            print(', ', end='')
        else:
            print('\n')


def factor_set(matrix, size):
    factor = [[(j + 1, i + 1) for j, value in enumerate(matrix[i]) if value == 1] for i in range(size)]
    factor.sort(key=len)

    factor_res = []
    factor_classes = []
    for i in range(size):
        for j in range(len(factor[i])):
            if not (factor[i][j][0] in factor_res):
                factor_res.append(factor[i][j][0])
                factor_classes.append(factor[i][j][1])
                i += 1
    return factor_res, factor_classes, factor


def make_equivalent_closure(copy, size):
    list_for_equivalent_closure = set()
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 1 and matrix[j][i] == 0:
                copy[j][i] = 1
            if copy[j][i]:
                list_for_equivalent_closure.add((j + 1, i + 1))
        if matrix[i][i] == 0:
            copy[i][i] = 1
        if copy[i][i]:
            list_for_equivalent_closure.add((i + 1, i + 1))

    for _ in range(size):
        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if copy[k][i] == copy[i][j] == 1 and copy[k][j] == 0:
                        copy[k][j] = 1
                    if copy[k][j]:
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
            if matrix[i][j] == matrix[j][i] == 1 and not i == j:
                flag_antisymmetric = False
            if not flag_symmetric and not flag_antisymmetric:
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


def hasse_greater_eq(nums):
    res = []
    res.append((nums[0], 1, []))
    for i, num in enumerate(nums[1:]):
        res.append((num, res[-1][1] + 1, [res[-1][0]]))
    return res


def hasse_division(dividers_num):
    hasse_list = []
    sl = {key: 1 if key == 1 else 0 for i, key in enumerate(dividers_num)}

    for number in dividers_num[1:]:
        for divider in dividers_num[:dividers_num.index(number)]:
            if number % divider == 0:
                sl[number] = sl[divider] + 1

    for k, v in sl.items():
        pod_res = []
        for k1, v1 in sl.items():
            if v1 + 1 == v and k % k1 == 0:
                pod_res.append(k1)
        hasse_list.append((k, v, pod_res))
    hasse_list.sort(key=lambda x: x[1])
    return hasse_list


def dividers(num, flag=False):
    result = []
    begin = 1
    if flag:
        begin = 2
    for i in range(begin, int(num / 2) + 1):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

#######################################################################################################################
matrix, matrix_set, size = get_data()
matrix_set_view(matrix_set)
print('\n')
print('Cвойства бинарного отношения:')
flagT = True
flagR = True
flagS = True

if is_transitive(matrix, size):
    print('Отношение является транзитивным')
else:
    print('Отношение не является транзитивным')
    flagT = False

symm, _ = is_symmetric_or_antisymmetric(matrix,size)
if symm:
    print('Отношение является симметричным')
else:
    print('Отношение не является симметричным')
    flagS = False

refl, _ = is_reflexive_or_anti_reflexive(matrix, size)
if refl:
    print('Отношение является рефлексивным')
else:
    print('Отношение не является рефлексивным')
    flagR = False

print('\n')
if not flagS or not flagR or not flagT:
    print('Так как отношение не обладает свойством ', end='')
    if not flagS:
        print('симметричности', end=', ')
    if not flagT:
        print('транзитивности', end=', ')
    if not flagR:
        print('рефлексивности', end=', ')
    print('то для получения фактор-множества отношения, требуется построить эквивалентное замыкание.')

    copy = matrix
    ls, mt = make_equivalent_closure(copy, size)

    print('Эквивалентное замыкание бинарного отношения: {', end='')
    print(*ls, sep=', ', end='}\n\n')

    print('Матрица эквивалентного замыкания бинарного отношения:')
    for i in range(len(mt)):
        print(*mt[i])
    print('\n')

    res_set, res_representatives, factor = factor_set(mt, size)
    print_factor(res_set, res_representatives, factor)

else:
    print('Заданное отношение является эквивалентным. Его матрица:')
    for i in range(len(matrix)):
        print(*matrix[i])
    print('\n')
    res_set, res_representatives, factor = factor_set(matrix, size)
    print_factor(res_set, res_representatives, factor)
#######################################################################################################################

print('\u13AF\u212C\u2642\u0392\u20B3')
for _ in range(7):
    print('\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694', end='')
print('\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694\u2694')


print('Выберите тип задания множества: число (1) или заданное множество (2)')
set_type = int(input())

print('Выберете тип порядка: <= (1) или отношение делимости (2)')
order_type = int(input())


num = None
res = None
if set_type == 1:
    print('Введите число')
    num = int(input())
    print('Хотите ли добавить единицу во множество? Да(1), Нет(0)')
    yes_or_no = int(input())
    sub_res = None
    if yes_or_no == 1:
        if order_type == 2:
            sub_res = dividers(num)
            res = hasse_division(sub_res)
        else:
            sub_res = [i + 1 for i in range(num)]
            res = hasse_greater_eq(sub_res)
    else:
        if order_type == 2:
            sub_res = dividers(num, True)
            res = hasse_division(sub_res)
        else:
            sub_res = [i + 2 for i in range(num - 1)]
            res = hasse_greater_eq(sub_res)
else:
    print('Введите множество')
    num = [int(value) for value in input().split()]
    num.sort()
    if order_type == 2:
        res = hasse_division(num)
    elif order_type == 1:
        res = hasse_greater_eq(num)

print(res)

print('Вы хотите получить диаграмму Хассе? Да(1) или Нет(0)')
yes_or_no = int(input())
if yes_or_no:
    # import ass
    # ass.main(res)
'''
Примеры входных данных:

3 
0 1 0
0 0 1
1 0 0

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

4
1 1 0 1
0 1 1 0 
0 0 1 1
0 0 0 1

4
1 0 1 0 
1 1 0 0
0 0 1 0
0 1 0 1

5
1 0 1 1 0
0 1 0 1 0
1 0 1 1 0
1 1 1 1 0
0 0 0 0 1
'''