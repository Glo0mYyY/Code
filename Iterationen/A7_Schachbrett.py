# Weiss = #, Schwarz = " "
n = 8
for i in range(0, n):
    for j in range(0, n):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(" ", end="")
    print()