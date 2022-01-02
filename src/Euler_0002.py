A, B, C, D = 1, 2, 0, 0

while A < 4000000 and B < 4000000:
    if B % 2 == 0:
        if D == 0:
            A += B
            D = 1
            C += B
        else:
            B += A
            D = 0
            C += B
        print(C)
    else:
        if D == 0:
            A += B
            D = 1
        else:
            B += A
            D = 0
