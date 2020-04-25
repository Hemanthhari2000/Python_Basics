n=int(input('Limit'))
i=2
while i<n:
    flag = True
    for item in range(2,int(i**0.5)+1):
        if i%item==0 and i!=item:
            flag = False
            break
    if flag:
        print(i)
    i+=1
