print('개수를 입력하세요')
count = int(input())
num = []
result = 0
print('숫자를 입력하세요')
num = [int(x) for x in input().split()]
if len(num) != count:
    print('입력하신 개수가 다릅니다.')
    exit()
num.sort()
for i in range(count):
    result += num[i] * ( count - i )
print(result)