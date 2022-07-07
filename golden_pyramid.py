import itertools


def get_best_value(row1, row2):
    combinations = list(itertools.product(row1, row2))
    max_value = sum(max(combinations, key=sum))
    print(f"Best is {max_value}")
    return max_value, max(combinations, key=sum)[1]


def pick_best_steps(row1, row2, best_value, previous=None):
    print(row2)
    print(row1)
    important_indexes = []
    values = []
    for index, value in enumerate(row2):
        if value + row1[index] == best_value or value + row1[index+1] == best_value:
            important_indexes.append(index)
            values.append(row2[index])
    return important_indexes, values


def count_gold(pyramid):
    cumulated_value = 0

    top_value = get_best_value(pyramid[-1], pyramid[-2])
    last_step_data = pick_best_steps(pyramid[-1], pyramid[-2], top_value[0])
    cumulated_value = cumulated_value + top_value[0]
    print(top_value, cumulated_value)

    top_value = get_best_value(last_step_data[1], pyramid[-3])
    last_step_data = pick_best_steps(pyramid[-2], pyramid[-3], top_value[0], last_step_data)
    cumulated_value = cumulated_value + top_value[1]
    print(top_value, cumulated_value)

    top_value = get_best_value(last_step_data[1], pyramid[-4])
    last_step_data = pick_best_steps(pyramid[-3], pyramid[-4], top_value[0], last_step_data)
    cumulated_value = cumulated_value + top_value[1]
    print(top_value, cumulated_value)

    top_value = get_best_value(last_step_data[1], pyramid[-5])
    last_step_data = pick_best_steps(pyramid[-4], pyramid[-5], top_value[0], last_step_data)
    cumulated_value = cumulated_value + top_value[1]
    print(top_value, cumulated_value)

    top_value = get_best_value(last_step_data[1], pyramid[-6])
    last_step_data = pick_best_steps(pyramid[-5], pyramid[-6], top_value[0], last_step_data)
    cumulated_value = cumulated_value + top_value[1]
    print(top_value, cumulated_value)

    top_value = get_best_value(last_step_data[1], pyramid[-7])
    last_step_data = pick_best_steps(pyramid[-6], pyramid[-7], top_value[0], last_step_data)
    cumulated_value = cumulated_value + top_value[1]
    print(top_value, cumulated_value)

    return cumulated_value


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    print("First ok! \n\n")
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
