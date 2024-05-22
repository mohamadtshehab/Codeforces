def solve():
    n = int(input())
    x = 0
    for _ in range(n):
        instruction = input()
        if instruction.__contains__('+'):
            x += 1
        elif instruction.__contains__('-'):
            x -= 1
    print(x)
    
solve()