with open("q5p1input-atom.txt", "r") as file:
    rule_list: list[list[int]] = [
        list(map(int, line.replace("\n", "").split("|"))) for line in file.readlines()
    ]
with open("q5p2input-atom.txt", "r") as file:
    sequences: list[list[int]] = [
        list(map(int, line.replace("\n", "").split(","))) for line in file.readlines()
    ]


def rule_list_to_rule_dict(rule_list: list[list[int]]):
    rule_dict: dict[int, list[int]] = {}
    reversed_rule_dict: dict[int, list[int]] = {}
    for x, y in rule_list:
        if x not in rule_dict:
            rule_dict[x] = [y]
        else:
            rule_dict[x].append(y)

        if y not in reversed_rule_dict:
            reversed_rule_dict[y] = [x]
        else:
            reversed_rule_dict[y].append(x)
    return rule_dict, reversed_rule_dict


def check_order(
    sequence: list[int],
    rule_dict: dict[int, list[int]],
    reversed_rule_dict: dict[int, list[int]],
) -> bool:
    for index, element in enumerate(sequence, start=0):
        following_elements: list[int] = sequence[index + 1 :]
        leading_elements: list[int] = sequence[:index]

        allowed_following_elements = rule_dict.get(element)
        allowed_leading_elements = reversed_rule_dict.get(element)

        correct_following_elements: list[int] = (
            [i for i in following_elements if (i in allowed_following_elements)]
            if (allowed_following_elements is not None)
            else None
        )
        correct_leading_elements: list[int] = (
            [i for i in leading_elements if i in allowed_leading_elements]
            if (allowed_leading_elements is not None)
            else None
        )

        if (correct_leading_elements is not None) and (
            len(correct_leading_elements) != len(leading_elements)
        ):
            return False
        if (correct_following_elements is not None) and (
            len(correct_following_elements) != len(following_elements)
        ):
            return False
    else:
        return True


def find_list_center(sequence: list[int]):
    return sequence[round(len(sequence) / 2 - 0.5)]


def sort_sequence(
    sequence: list[int],
    rule_dict: dict[int, list[int]],
    reversed_rule_dict: dict[int, list[int]],
):
    # Gradually inserting elements at the end. Swap until that element is sorted
    sorted_list: list[int] = [sequence[0]]
    for element in sequence:
        for index in range(len(sorted_list), -1, -1):
            test_list: list[int] = sorted_list.copy()
            test_list.insert(index, element)
            if check_order(test_list, rule_dict, reversed_rule_dict):
                sorted_list.insert(index, element)
                break
    return sorted_list


rule_dict, reversed_rule_dict = rule_list_to_rule_dict(rule_list)
result = 0
for sequence in sequences:
    if not check_order(sequence, rule_dict, reversed_rule_dict):
        sorted_sequence = sort_sequence(sequence, rule_dict, reversed_rule_dict)
        list_center = find_list_center(sorted_sequence)
        result += list_center
result