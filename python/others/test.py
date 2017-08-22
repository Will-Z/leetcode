# -*- coding: utf-8 -*-

# 杨辉三角 generator

def triangles():
    maxline = 100

    m = [[0 for i in range(maxline)] for j in range(maxline)]

    for i in range(maxline):
        m[i][i] = 1

    for i in range(maxline):
        row = []
        for j in range(i):
            if j == 0:
                m[i][j] = 1
                row.append(m[i][j])
                continue
            m[i][j] = m[i - 1][j] + m[i - 1][j - 1]
            row.append(m[i][j])
        m[i][i] = 1
        row.append(m[i][i])
        yield row




# test
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break