A = input()
d1 = A[0]
d2 = A[1]
d3 = A[2]
d4 = A[3]
d5 = A[5]

if A.count('?') == 0 :
    if d5 == 'X' and (int(d1) * 2 + int(d2) * 3 + int(d3) * 5 + int(d4) * 7) % 11 == 10 :
        print("VALID")
    elif d5 != 'X' and int(d5) == (int(d1) * 2 + int(d2) * 3 + int(d3) * 5 + int(d4) * 7) % 11 :
        print("VALID")
    else:
        print("INVALID")

elif d5 == '?' and A.count('?') == 1 :
    if (int(d1) * 2 + int(d2) * 3 + int(d3) * 5 + int(d4) * 7) % 11 == 10 :
        print(A[0:5] + 'X')
    else:
        CheckDigit = (int(d1) * 2 + int(d2) * 3 + int(d3) * 5 + int(d4) * 7) % 11
        print(A[0:5] + str(CheckDigit))

elif d1 == '?' and A.count('?') == 1 :
    if d5 == 'X' :
        a = int(10 - ((int(d2) * 3 + int(d3) * 5 + int(d4) * 7) % 11))
        a1 = (6 * a) % 11
        print(str(a1) + A[1:])
    else:
        b = int(int(d5) + 11 - ((int(d2) * 3 + int(d3) * 5 + int(d4) * 7) % 11))
        b1 = (6 * b) % 11
        print(str(b1) + A[1:])

elif d2 == '?' and A.count('?') == 1 :
    if d5 == 'X' :
        c = int(10 - ((int(d1) * 2 + int(d3) * 5 + int(d4) * 7) % 11))
        c2 = (4 * c) % 11
        print(d1 + str(c2) + A[2:])
    else:
        e = int(int(d5) + 11 - ((int(d1) * 2 + int(d3) * 5 + int(d4) * 7) % 11))
        e2 = (4 * e) % 11
        print(d1 + str(e2) + A[2:])

elif d3 == '?' and A.count('?') == 1 :
    if d5 == 'X' :
        f = int(10 - ((int(d1) * 2 + int(d2) * 3 + int(d4) * 7) % 11))
        f3 = (9 * f) % 11
        print(A[:2] + str(f3) + A[3:])
    else:
        g = int(int(d5) + 11 - ((int(d1) * 2 + int(d2) * 3 + int(d4) * 7) % 11))
        g3 = (9 * g) % 11
        print(A[:2] + str(g3) + A[3:])

elif d4 == '?' and A.count('?') == 1 :
    if d5 == 'X' :
        h = int(10 - ((int(d1) * 2 + int(d2) * 3 + int(d3) * 5) % 11))
        h4 = (8* h) % 11
        print(A[:3] + str(h4) + A[4:])
    else:
        i = int(int(d5) + 11 - ((int(d1) * 2 + int(d2) * 3 + int(d3) * 5) % 11))
        i4 = (8 * i) % 11
        print(A[:3] + str(i4) + A[4:])

else:
    print("INVALID")