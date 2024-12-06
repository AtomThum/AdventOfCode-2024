import numpy as np
import itertools as itr

unitXDiag = np.array([1, -1, -1, 1])
unitYDiag = np.array([-1, -1, 1, 1])


with open("q4input-atom.txt", "r") as file:
    text = np.array(
        [[char for char in line.replace("\n", "")] for line in file.readlines()]
    )


def findBigXMAS(y: int, x: int, text: np.array) -> int:
    # If at the edge, stop scanning immediately
    if text[y, x] != "A":
        return 0

    # Check if it's out of bound or not
    for i, (cx, cy) in enumerate(zip(unitXDiag, unitYDiag)):
        if not (0 <= y + cy < text.shape[0] and 0 <= x + cx < text.shape[1]):
            return 0

    # Check for the letter M counterclockwise.
    for i, (cx, cy) in enumerate(zip(unitXDiag, unitYDiag)):
        if text[y + cy, x + cx] == "M":
            mDir0 = i
            break
    else:
        return 0

    # Define relative direction from mDir0, going counter clockwise
    mDir1 = (mDir0 + 1) % 4  #
    mDir2 = (mDir0 + 2) % 4  #
    mDir3 = (mDir0 + 3) % 4  #

    yDir1, xDir1 = unitYDiag[mDir1], unitXDiag[mDir1]
    yDir2, xDir2 = unitYDiag[mDir2], unitXDiag[mDir2]
    yDir3, xDir3 = unitYDiag[mDir3], unitXDiag[mDir3]

    textDir1 = text[y + yDir1, x + xDir1]
    textDir2 = text[y + yDir2, x + xDir2]
    textDir3 = text[y + yDir3, x + xDir3]

    # There could only be two cases:
    # M at counter-clockwise - mDir1 = M, mDir2 = mDir3 = S
    # M at clockwise - mDir3 = M, mDir1 = mDir2 = S

    if (textDir1 == "M" and textDir2 == "S" and textDir3 == "S") or (
        textDir3 == "M" and textDir1 == "S" and textDir2 == "S"
    ):
        return 1
    else:
        return 0

XMASAmount = sum(findBigXMAS(xIndex, yIndex, text) for xIndex, yIndex in itr.product(range(140), range(140)))
print(XMASAmount)