def solve():
    n, k = [int(i) for i in input().split(' ')]
    scores = [int(i) for i in input().split(' ')]
    k_score = scores[k-1]
    count = 0
    for i in range(n):
        if scores[i] > 0:
            if scores[i] >= k_score:
                count += 1
            else:
                break
    print(count)
    
solve()