import numpy as np

file = open("q2input-atom.txt", "r")
sequenceList = [
    list(map(int, line.replace("\n", "").split(sep=" "))) for line in file.readlines()
]
file.close()


def isSafe(sequence: np.array):
    sortedSequence = np.sort(sequence)
    if np.array_equal(sequence, sortedSequence) or np.array_equal(
        np.flip(sequence), sortedSequence
    ):
        sequence = np.append(sequence, [0])
        rolledSequence = np.roll(sequence, 1)
        differences = np.absolute(sequence - rolledSequence)[1:-1]
        for difference in differences:
            if difference > 3 or difference < 1:
                break
        else:
            return True
    else:
        return False


def isSafeRemove(sequence: np.array, removePos: int):
    return isSafe(np.delete(sequence, removePos))


safeSequencesAmount = 0
for sequence in sequenceList:
    sequence = np.array(sequence)
    if isSafe(sequence):
        safeSequencesAmount += 1
    else:
        for removePos in range(len(sequence)):
            if isSafeRemove(sequence=sequence, removePos=removePos):
                safeSequencesAmount += 1
                break
print(safeSequencesAmount)
