def question(request):
    coin = [500,100,50,10]
    count = 0
    for c in coin:
        count += request // c
        request %= c
    return count

print("값을 입력하세요.")
print(question(int(input())))
# https://github.com/e3hope/Algorithm