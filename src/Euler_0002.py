A, B ,C, sum = 1, 2, 0, 0

while B < 4000000:

    if B % 2 == 0:
        sum += B
    C = A + B
    A = B
    B = C
print(sum)