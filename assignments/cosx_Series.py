import math
def cos(x,n):
    cosine=0
    for i in range(n):
        sign=(-1)**i
        pi=22/7
        y=x*(pi/180)
        cosine=cosine+((y**(2.0*i))/math.factorial(2*i))*sign
    return cosine
x=int(input('Enter x : '))
n=int(input('Enter n : '))
print (round(cos(x,n),2))
