    
def pascal_triangle(n):
    a = []
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(0)
    for i in range(n):
        for j in range(n):
            if i == j: a[i][j] = 1
            elif j == 0: a[i][j] = 1
            else:
                a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in a:
        print(*i)
pascal_triangle(6)