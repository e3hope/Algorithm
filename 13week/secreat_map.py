def match(num,map1,map2):
    for n in range(num):
        m1 = format(map1[n],'b')
        m2 = format(map2[n],'b')
        max_num = max(len(m1),len(m2))
        m1 = m1.rjust(max_num,'0')
        m2 = m2.rjust(max_num,'0')
        array = []
        for l in range(len(str(m1))):
            temp = 0 if m1[l] == '0' and m2[l] == '0'  else 1
            array.append(temp)
        
        for a in array:
            print ( '#' if a == 1 else ' ',end=' ')
        print(sep='\n')
num = int(input())
map1 = list(map(int, input().split()))
map2 = list(map(int, input().split()))
match(num,map1,map2)