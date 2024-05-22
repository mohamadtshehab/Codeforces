def solve():
    string = input()
    if len(string) < 8:
        print('NO')
    else:
        one_count = 0
        zero_count = 0
        for char in string:
            if char == '0':
                one_count = 0
                zero_count += 1
            elif char == '1':
                zero_count = 0
                one_count += 1
            if one_count == 7 or zero_count == 7:
                print('YES')
                return
        print('NO')
solve()