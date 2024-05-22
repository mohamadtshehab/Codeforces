def solve():
    n = int(input())
    coins = [int(i) for i in input().split(' ')]
    coins.sort(reverse=True)
    coin_sum = 0
    for i, coin in enumerate(coins):
        coin_sum += coin
        rest_sum = sum(coins[i+1:])
        if coin_sum > rest_sum:
            print(i+1)
            return

solve()
        