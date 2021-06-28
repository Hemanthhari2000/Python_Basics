n=int(input('Enter Number: '))
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
print('Sum of Digits is ',sum)
    
