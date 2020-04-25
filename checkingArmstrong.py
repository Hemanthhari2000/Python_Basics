n=int(input('Enter the number:  '))
sum=0
temp=n
while n>0:
    r=n%10
    sum+=r**3
    n//=10
if temp==sum:
    print ('It is an ARMSTRONG NUMBER')
else:
    print('It is NOT an ARMSTRONG NUMBER')
