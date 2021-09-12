def question(request):
    coin = [500,100,50,10]
    count = 0
    for c in coin:
        count += request // c
        request %= c
    return count

print(question(1260))