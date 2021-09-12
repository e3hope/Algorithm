def question(coin,money):
    count = 0
    for c in coin:
        count += money // c
        money %= c
    return count

print("값을 입력하세요.동전개수와 금액")
coin_count, money = map(int, input().split())
coin = []
for c in range(coin_count):
    temp = int(input())
    coin.append(temp)
coin.reverse()
print(question(coin,money))
# https://github.com/e3hope/Algorithm