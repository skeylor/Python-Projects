N = int(input())
nMinsOne = N - 1
sumDiag1 = 0
sumDiag2 = 0

for i in range(N):
    line = input().split()
    sumDiag1 += int(line[i])
    sumDiag2 += int(line[nMinsOne - i])

print (abs(sumDiag1 - sumDiag2))