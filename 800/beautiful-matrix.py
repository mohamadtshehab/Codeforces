def solve():
    matrix = []
    one_index = ()
    for i in range(5):
        row = [int(k) for k in input().split(' ')]
        for j, item in enumerate(row):
            if row[j] == 1:
                one_index = (i, j)
    distance = abs(one_index[0] - 2) + abs(one_index[1] - 2)
    print(distance)
    
solve()