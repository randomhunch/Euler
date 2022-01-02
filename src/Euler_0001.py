sum = 0
N = 0

while N < 1000:
    if N%3==0 or N%5==0:
        sum += N
    N += 1

print(sum)