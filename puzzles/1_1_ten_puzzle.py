import re


def solve(num, in_data):
    """
    テンパズルを解く。
    Brute force searchはとりあえず考えなしにやったものでバグがあり、Q11が解けない。
    正攻法は逆ポーランド記法で解く。
    :param num:
    :param in_data:
    :return:
    """
    print(f'=== Q{num} ===')

    b = by_brute_force_search(in_data)
    print(f'[B] Q{num}: {in_data} -> {b} = 10')

    p = by_reverse_polish_notation(in_data)
    print(f'[P] Q{num}: {in_data} -> {p} = 10')

    if b.replace(' ', '') == p.replace(' ', ''):
        print('correct')
    else:
        print('incorrect')


def by_brute_force_search(in_data):
    """
    brute force search (力まかせ探索) で解く
    :param num:
    :param in_data:
    :return:
    """
    # print(f'in data: {in_data}')
    operators = ['+', '-', '*', '/']

    num_patterns = get_num_patterns(in_data)
    # print(f'num_patterns: {num_patterns}')

    result = ''
    for x in range(4):
        for y in range(4):
            for z in range(4):
                for n in num_patterns:
                    try:
                        result = calculate(n, operators, x, y, z)
                    except ZeroDivisionError:
                        continue
                    if result != '':
                        break
                if result != '':
                    break
            if result != '':
                break
        if result != '':
            break
    return result


def calculate(n, o, x, y, z):
    brace_patterns = [
        ['', '', '', '', '', '', '', ''],
        ['(', '', '', ')', '', '', '', ''],
        ['(', '', '', '', '', ')', '', ''],
        ['', '', '(', '', '', ')', '', ''],
        ['', '', '(', '', '', '', '', ')'],
        ['', '', '', '', '(', '', '', ')'],
        ['(', '', '', ')', '(', '', '', ')'],
    ]

    for b in brace_patterns:
        result = f'{b[0]} {n[0]} {b[1]} {o[x]} {b[2]} {n[1]} {b[3]} {o[y]} {b[4]} {n[2]} {b[5]} {o[z]} {b[6]} {n[3]} {b[7]}'
        if eval(result) == 10:
            return result
    return ''


def by_reverse_polish_notation(in_data):
    """
    逆ポーランド記法 (Reverse Polish Notation) で解く
    :param num:
    :param in_data:
    :return:
    """
    num_patterns = get_num_patterns(in_data)

    result = ''
    operators = '+-*/'
    for op1 in operators:
        for op2 in operators:
            for op3 in operators:
                for n in num_patterns:
                    # try all patterns (only 5 patterns)
                    formula_1 = f'{n[0]}{n[1]}{n[2]}{n[3]}{op1}{op2}{op3}'
                    r = calc_polish(formula_1)
                    if r == 10:
                        result = decode_polish(formula_1)
                        break
                    formula_2 = f'{n[0]}{n[1]}{n[2]}{op1}{n[3]}{op2}{op3}'
                    r = calc_polish(formula_2)
                    if r == 10:
                        result = decode_polish(formula_2)
                        break
                    formula_3 = f'{n[0]}{n[1]}{n[2]}{op1}{op2}{n[3]}{op3}'
                    r = calc_polish(formula_3)
                    if r == 10:
                        result = decode_polish(formula_3)
                        break
                    formula_4 = f'{n[0]}{n[1]}{op1}{n[2]}{n[3]}{op2}{op3}'
                    r = calc_polish(formula_4)
                    if r == 10:
                        result = decode_polish(formula_4)
                        break
                    formula_5 = f'{n[0]}{n[1]}{op1}{n[2]}{op2}{n[3]}{op3}'
                    r = calc_polish(formula_5)
                    if r == 10:
                        result = decode_polish(formula_5)
                        break
                if result != '':
                    break
            if result != '':
                break
        if result != '':
            break

    return result


def calc_polish(formula):
    stack = []
    for f in formula:
        if re.match('[0-9]', f):
            stack.append(int(f))
        elif len(stack) > 1:
            second = stack.pop()
            first = stack.pop()
            try:
                stack.append(eval(f'{first} {f} {second}'))
            except ZeroDivisionError:
                continue

    if len(stack) > 0:
        return stack.pop()
    return None


def decode_polish(formula):
    """
    逆ポーランド記法で書かれた数式を、一般的な数式に変換する
    :param formula:
    :return:
    """
    stack = []
    for f in formula:
        if re.match('[0-9]', f):
            stack.append(f)
        else:
            second = stack.pop()
            first = stack.pop()
            if f == '*' or f == '/':
                if len(first) > 1:
                    first = f'( {first} )'
                if len(second) > 1:
                    second = f'( {second} )'
            stack.append(f'{first} {f} {second}')
    return stack.pop()


def get_num_patterns(in_data):
    """
    与えられた入力データの全ての組み合わせを返す
    :param in_data:
    :return:
    """
    num_patterns = []

    s_data = sorted(in_data)
    for a in range(4):
        for b in range(4):
            if b == a:
                continue
            for c in range(4):
                if c == a or c == b:
                    continue
                for d in range(4):
                    if d == a or d == b or d == c:
                        continue
                    num_patterns.append([s_data[a], s_data[b], s_data[c], s_data[d]])
    return num_patterns


if __name__ == '__main__':
    test_data = [
        [1, 2, 3, 4],
        [1, 3, 5, 7],
        [1, 1, 2, 5],
        [1, 1, 2, 4],
        [1, 1, 1, 6],
        [1, 2, 7, 7],
        [5, 5, 5, 7],
        [9, 9, 9, 9],
        [1, 3, 3, 7],
        [1, 1, 9, 9],
        [1, 1, 5, 8],
        [3, 4, 7, 8],
    ]
    for data in test_data:
        solve(test_data.index(data) + 1, data)
