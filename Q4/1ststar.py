import numpy as np
import itertools as itr

with open("q4input-atom.txt", "r") as file:
    text = np.array(
        [[char for char in line.replace("\n", "")] for line in file.readlines()]
    )

unitY = np.array([0, 1, 0, -1, 1, 1, -1, -1])
unitX = np.array([1, 0, -1, 0, 1, -1, -1, 1])


# Implementing depth first search:
def searchXMAS(y: int, x: int, text: np.array) -> int:
    XMASAmount = 0

    if text[y, x] != "X":
        return 0

    # Find the direction of M's
    mDirection = []
    for i, (cy, cx) in enumerate(zip(unitY, unitX)):
        if (
            0 <= y + cy < text.shape[0]
            and 0 <= x + cx < text.shape[1]
            and text[y + cy, x + cx] == "M"
        ):
            mDirection.append(i)

    # Filter through the M's direction and find the one with A's and S's
    textSizeY = text.shape[0]
    textSizeX = text.shape[1]
    for i in mDirection:
        cy, cx = unitY[i], unitX[i]
        if (
            0 <= y + 2 * cy < textSizeY
            and 0 <= y + 3 * cy < textSizeY
            and 0 <= x + 2 * cx < textSizeX
            and 0 <= x + 3 * cx < textSizeX
        ):
            if (
                text[y + 2 * unitY[i], x + 2 * unitX[i]] == "A"
                and text[y + 3 * unitY[i], x + 3 * unitX[i]] == "S"
            ):
                XMASAmount += 1
    return XMASAmount


XMASAmount = sum(
    searchXMAS(yIndex, xIndex, text)
    for yIndex, xIndex in itr.product(range(text.shape[0]), range(text.shape[1]))
)
print(XMASAmount)
