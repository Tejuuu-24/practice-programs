n = int(input())

square = n * n
digits = len(str(n))

if square % (10 ** digits) == n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")