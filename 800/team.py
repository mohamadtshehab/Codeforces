def solve():
    n = int(input())
    count = 0
    for _ in range(n):
        yes_count = 0
        decisions = input()
        for char in decisions:
            if not char.isspace():
                if char == '1':
                    yes_count += 1
        if yes_count >= 2:
            count += 1
    print(count)
    
solve()