import re

pattern = r"mul\((-?\d+),\s*(-?\d+)\)"
with open("q3input-atom.txt", "r") as file:
    print(
        sum(
            int(x) * int(y)
            for line in file
            for (x, y) in re.findall(pattern=pattern, string=line)
        )
    )
