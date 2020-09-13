
import random, math
import matplotlib.pyplot as plt




MSE = [0,0,0,0,0,0,0,0,0,0,0]
counts = [0,0,0,0,0,0]
averageError = [0,0,0,0,0,0,0,0,0,0,0]
FractionalAverageError = [0,0,0,0,0,0,0,0,0,0,0]
FractionalError = [0,0,0,0,0,0,0,0,0,0,0]
numTrial = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000]
normalized_error = []
face_one = []
for trail in range(1, 10000):

    x = random.randint(1,59)

    if 0 <= x <= 9:
        counts[0] += 1
    if 10 <= x <= 19:
        counts[1] += 1
    if 20 <= x <= 29:
        counts[2] += 1
    if 30 <= x <= 39:
        counts[3] += 1
    if 40 <= x <= 49:
        counts[4] += 1
    if 50 <= x <= 59:
        counts[5] += 1

    error = 0
    face_one.append(counts[0]/trail)
    for c in counts:
        error +=  c - trail/ 6

    normalized_error.append(error/trail)

    # FractionalError[y] = int((counts[0] - numTrial[y]) / numTrial[y] * 100 + (counts[1] - numTrial[y]) / numTrial[y] * 100 + (counts[2] - numTrial[y]) / numTrial[y] * 100 + (counts[3] - numTrial[y]) / numTrial[y] * 100 + (counts[4] - numTrial[y]) / numTrial[y] * 100 + (counts[5] - numTrial[y]) / numTrial[y] * 100)

    # FractionalAverageError[y] = averageError[y] / numTrial[y]
    # MSE[y] = 1/6 * math.sqrt((counts[0] - numTrial[y] / 6)**2  + (counts[1] - numTrial[y] / 6)**2  + (counts[2] - numTrial[y] / 6)**2  + (counts[3] - numTrial[y] / 6)**2  + (counts[4] - numTrial[y] / 6)**2  + (counts[5] - numTrial[y] / 6)**2)

print(normalized_error)
# print(FractionalError)



plt. xlabel("Number of trials")
plt. ylabel("Absolute error")
plt.plot()
plt.title("My graph")
plt.plot(normalized_error, label ="Test", color = "k")
plt.show()

