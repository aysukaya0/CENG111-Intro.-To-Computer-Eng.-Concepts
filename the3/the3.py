def forward_pass(Network,X):
    i = 0
    while i < len(Network):
        if type(Network[i]) == list:
            linear = Network[i][1]
            newX = []
            x = 0
            while x < len(linear):
                value = 0
                for y in range(len(X)):
                    a = X[y] * linear[x][y]
                    value += float(a)
                newX.append(value)
                x += 1
            X = newX
        elif Network[i][0] == 'r':
            z = 0
            while z < len(X):
                if X[z] <= 0:
                    X[z] = 0
                z += 1
        else:
            t = 0
            while t < len(X):
                X[t] = sigmoid(X[t])
                t += 1
        i += 1
    return X

def sigmoid(n):
    import math
    if n <= -700:
        return 0
    elif n > -700 and n < 700:
        return 1 / (1 + math.exp(-n))
    else:
        return 1