def solve(target_num, in_data):
    print(f'=== [by brute force search] ===')
    b_results = by_brute_force_search(target_num, in_data)
    for b_result in b_results:
        print(f'{b_result}=100')

    print(f'=== [by recursive search] ===')
    by_recursive_search(target_num, in_data, [])


def by_brute_force_search(target_num, in_data):
    results = []
    operators = ['', '+', '-', '*', '/']
    for a in operators:
        for b in operators:
            for c in operators:
                for d in operators:
                    for e in operators:
                        for f in operators:
                            for g in operators:
                                for h in operators:
                                    formula = f'{in_data[0]}{a}{in_data[1]}{b}{in_data[2]}{c}{in_data[3]}{d}{in_data[4]}{e}{in_data[5]}{f}{in_data[6]}{g}{in_data[7]}{h}{in_data[8]}'
                                    result = eval(formula)
                                    if result == target_num:
                                        results.append(formula)
                                        break

    return results


def by_recursive_search(target_num, in_data, current):
    """
    Search for a formula that satisfies the target value recursively.

    :param target_num: Target value of calculation results
    :param in_data: List of numbers
    :param current: current operator list
    :return: current operator list
    """
    operators = ['', '+', '-', '*', '/']

    if len(current) >= len(in_data) - 1:
        print_result(target_num, in_data, current)
        return current

    for o in operators:
        current.append(o)
        current = by_recursive_search(target_num, in_data, current)
        current = current[:-1]
    return current


def print_result(target_num, in_data, current):
    result = []
    for i in range(len(in_data)):
        result.append(str(in_data[i]))
        if i < len(current):
            result.append(current[i])
    formula = ''.join(result)
    if eval(formula) == target_num:
        print(f'{formula}={target_num}')


if __name__ == '__main__':
    target_num = 100
    test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solve(target_num, test_data)
