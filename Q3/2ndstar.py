import re

patternDoDont = r"do\(\)(.*?)don't\(\)"
patternMul = r"mul\((-?\d+),\s*(-?\d+)\)"
patternFirstBlock = r"^(.*?)(?=do\(\)|don't\(\))"
with open("q3input-atom.txt", "r") as file:
    textList = [line.replace("\n", "") for line in file.readlines()]
    text = "".join(textList)

firstBlock = re.findall(pattern=patternFirstBlock, string=text)[0]
sumFirstBlock = sum(
    int(x) * int(y) for (x, y) in re.findall(pattern=patternMul, string=firstBlock)
)

doDontBlockItr = re.findall(pattern=patternDoDont, string=text)
sumDoDontBlock = sum(
    int(x) * int(y)
    for doDontBlock in doDontBlockItr
    for (x, y) in re.findall(pattern=patternMul, string=doDontBlock)
)
print(sumDoDontBlock + sumFirstBlock)
