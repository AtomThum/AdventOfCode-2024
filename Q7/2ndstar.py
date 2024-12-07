with open("q7input-atom.txt", "r") as file:
    equations: list = []
    for line in file.readlines():
        temp: list = line.split(": ")
        temp[0] = int(temp[0])
        temp[1] = list(map(int, temp[1].replace("\n", "").split(" ")))
        equations.append(temp)


def to_ternary(number: int, ternary_length: int) -> str:
    if number == 0:
        ternary: str = "0"
    ternary: str = ""
    while number > 0:
        ternary = str(number % 3) + ternary
        number //= 3
    return ternary.zfill(ternary_length)


def is_valid_add_mul_concat(sequence: list[int, list[int]]) -> bool:
    target, operands = sequence
    operation_length: int = len(operands) - 1
    for index in range(3**operation_length):
        # Loop backwards
        ternary_index: str = to_ternary(index, ternary_length=operation_length)[::-1]
        result: int = operands[0]
        for index, operator_index in enumerate(ternary_index, start=1):
            match operator_index:
                case "0":
                    result += operands[index]
                case "1":
                    result *= operands[index]
                case "2":
                    result = int(str(result) + str(operands[index]))
        if result == target:
            return True
    else:
        return False


print(sum(equation[0] for equation in equations if is_valid_add_mul_concat(equation)))
