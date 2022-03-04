def make_nums_obj_attr(objects, attributes):
    return {key: i for i, key in enumerate(objects)}, {key: i for i, key in enumerate(attributes)}


def get_lattice_of_concepts(matrix, size, keys):
    closure_system = set()
    subsets_attrs = dict()
    all_subsets = set([i + 1 for i in range(size)])
    for i in range(size):
        new_subset = []
        for j in range(size):
            if matrix[j][i] == 1:
                new_subset.append(j + 1)
        new_subset = frozenset(new_subset)
        all_subsets = all_subsets.intersection(new_subset)
        if not closure_system:
            closure_system.add(new_subset)
            subsets_attrs[keys[i]] = new_subset
        else:
            subsets = set()
            for subset in closure_system:
                subsubset = frozenset(subset.intersection(new_subset))
                if subsubset:
                    for key, value in subsets_attrs.items():
                        if value == subset:
                            subsets_attrs[f'{key}, {keys[i]}'] = subsubset
                            break
                    subsets.add(subsubset)
            for subset in subsets:
                closure_system.add(subset)
            if new_subset not in closure_system:
                closure_system.add(new_subset)
                subsets_attrs[f'{keys[i]}'] = new_subset
    set_for_g = '\u2205'
    for key, value in subsets_attrs.items():
        if all_subsets == value:
            set_for_g = value
            break
    return subsets_attrs, f'(G, {set_for_g})'


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
    print('\n')


def print_closure_system(dictionary):
    print('Z_f_G = {G, \u2205, ', end='')
    for value in dictionary[:-1:]:
        value = list(value)
        print('{', end='')
        print(*value, sep=',', end='}, ')
    print('{', end='')
    print(*dictionary[-1], sep=', ', end='}')
    print('}\n')


def intersections(sets):
    result = []
    for i, subset in enumerate(sets):
        podres = [subset, 1, []]
        for j, subset1 in enumerate(sets):
            if not subset1[0].difference(subset[0]) and not subset1[0] == subset[0]:
                podres[2].append(set(subset1[0]))
        result.append(podres)

    for subset in result:
        for subset1 in result:
            if not subset1[0][0].difference(subset[0][0]) and not subset1[0][0] == subset[0][0]:
                subset[1] = subset1[1] + 1

    return sorted([tuple(val) for val in result], key=lambda x: x[1])


def print_lattice_of_concepts(mat, attr):
    lattice_of_concepts, g = get_lattice_of_concepts(mat, len(attr), list(attr.keys()))
    lattice_of_concepts_save = lattice_of_concepts.copy()
    for key, value in lattice_of_concepts.items():
        for key1, value1 in lattice_of_concepts.items():
            if value == value1 and not key == key1:
                if min(key, key1) in lattice_of_concepts_save:
                    lattice_of_concepts_save.pop(min(key, key1))
    print('Система замыканий: ', end='')
    print_closure_system(list(lattice_of_concepts_save.values()))
    print('Включения-исключения))): ')
    print(intersections([(set(v), set(k.replace(',', ' ').split())) for k, v in lattice_of_concepts_save.items()]))

    # import hasse_visualization as hs
    # hs.visual(res)
    print('Решетка концептов C(K) состоит из элементов: ', end='')
    for key, value in lattice_of_concepts_save.items():
        value = list(value)
        print('({', end='')
        print(*value, sep=',', end='},')
        print('{' + key + '}', end='), ')

    print(g, end=', ')
    print('(\u2205, M)')


def main():
    print('Введите множество объектов')
    # obj = [int(value) for value in input().split()]
    obj = [1, 2, 3, 4]
    print('Введите множество атрибутов')
    # attr = input().split()
    attr = ['a', 'b', 'c', 'd']
    obj, attr = make_nums_obj_attr(obj, attr)

    # mat = get_matrix(len(attr))
    # mat = [[0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 1]]
    mat = [[1, 0, 1, 0], [1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1]]
    print_matrix(mat, obj)
    print_lattice_of_concepts(mat, attr)


main()
