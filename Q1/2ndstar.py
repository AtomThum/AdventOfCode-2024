import numpy as np

_ = np.loadtxt("q1input-atom.txt", dtype = "int")
leftList = _[:, 0]
rightList = _[:, 1]

rightUnique, rightCount = np.unique(rightList, return_counts=True)
rightDict = dict(zip(rightUnique, rightCount))

similarity = 0
for i in leftList:
    try: 
        similarity += i * rightDict[i]
    except KeyError:
        similarity += 0

print(similarity)