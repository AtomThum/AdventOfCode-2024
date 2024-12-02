import numpy as np

file = open("q2input-atom.txt", "r")
sequenceList = [
    list(map(int, line.replace("\n", "").split(sep=" "))) for line in file.readlines()
]
file.close()

safeSequencesAmount = 0
for sequence in sequenceList:
    sequence = np.array(sequence)
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
            safeSequencesAmount += 1
    else:
        pass

print(safeSequencesAmount)
