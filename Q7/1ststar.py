with open("q7input-atom.txt", "r") as file:
    equations: list = []
    for line in file.readlines():
        temp: list = line.split(": ")
        temp[0] = int(temp[0])
        temp[1] = list(map(int, temp[1].replace("\n", "").split(" ")))
        equations.append(temp)


def to_binary(number: int, binary_length: int) -> str:
    return format(number, f"0{binary_length}b")


def is_valid(sequence: list[int, list[int]]) -> bool:
    target, operands = sequence
    operation_length: int = len(operands) - 1
    for index in range(2**operation_length):
        binary_index: str = to_binary(index, binary_length=operation_length)[::-1]
        result: int = operands[0]
        for index, operator_index in enumerate(binary_index, start=1):
            if operator_index == "0":
                result += operands[index]
            else:
                result *= operands[index]
        if result == target:
            return True
    else:
        return False


print(sum(equation[0] for equation in equations if is_valid(equation)))
