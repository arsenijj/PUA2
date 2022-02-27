def make_nums_obj_attr(objects, attributes):
    return {value: i for i, value in enumerate(objects)}, {value: i for i, value in enumerate(attributes)}


def get_rho_minus_attr(matrix, size):
    closure_system = set()
    for i in range(size):
        new_subset = []
        for j in range(size):
            if matrix[j][i] == 1:
                new_subset.append(j + 1)
        new_subset = frozenset(new_subset)
        if not closure_system:
            closure_system.add(new_subset)
        else:
            sets = []
            for subset in closure_system:
                new_subset = frozenset(subset.intersection(new_subset))
                sets.append(new_subset)
            for subset in sets:
                closure_system.add(subset)
            closure_system.add(new_subset)
    return closure_system


def get_matrix(size):
    print(f'Введите значения матрицы бинарного отношения построчно (по {size})')
    return [[int(value) for value in input().split()] for _ in range(size)]


def print_matrix(mat, obj):
    print('  ', end='')
    print(*obj)
    symbols = list(obj.keys())
    for i in range(len(mat)):
        print(symbols[i], end=' ')
        print(*mat[i])

# print('Введите множество объектов')
# obj = [int(value) for value in input().split()]
#
# print('Введите множество атрибутов')
# attr = input().split()
#
# obj, attr = make_nums_obj_attr(obj, attr)
#
# mat = get_matrix(len(attr))
#
# print_matrix(mat, obj)
# print(get_rho_minus_attr(mat, len(attr)))

'''
1 2 3 4

a b c d

1 0 1 0
1 1 0 0
0 1 0 1
0 1 0 1
'''