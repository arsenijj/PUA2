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


def print_matrix(mat, attr, obj):
    print('  ', end='')
    print(*list(attr.keys()))
    obj = list(obj.keys())
    for i in range(len(mat)):
        print(obj[i], end=' ')
        print(*mat[i])


def print_lattice_of_concepts(mat, attr):
    print('Решетка концептов C(K) состоит из элементов: ', end='')
    lattice_of_concepts, g = get_lattice_of_concepts(mat, len(attr), list(attr.keys()))
    for key, value in lattice_of_concepts.items():
        value = list(value)
        print('({', end='')
        print(*value, sep=',', end='},')
        print('{' + key + '}', end='), ')

    print(g, end=', ')
    print('(\u2205, M)')


def main():
    print('Введите множество объектов')
    obj = [int(value) for value in input().split()]

    print('Введите множество атрибутов')
    attr = input().split()

    obj, attr = make_nums_obj_attr(obj, attr)

    mat = get_matrix(len(attr))

    print_matrix(mat, attr, obj)
    print_lattice_of_concepts(mat, attr)
