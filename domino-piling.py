def solve():
    m, n = [int(i) for i in input().split(' ')]
    size = m * n
    if size % 2 != 0:
        size = size - 1
    print(int(size/2))
    
solve()