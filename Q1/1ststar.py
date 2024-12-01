import numpy as np

_ = np.loadtxt("q1input-atom.txt", dtype = "int")
leftList = _[:, 0]
rightList = _[:, 1]

leftSorted = np.sort(leftList)
rightSorted = np.sort(rightList)

print(np.sum(np.abs(leftSorted - rightSorted)))