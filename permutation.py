def permutation(a, b, c):
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                yield a[i] + b[j] + c[k]

                