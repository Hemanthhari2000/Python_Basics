list=[]
n=int(input('Size Of Array/List'))
for i in range(0,n):
    x=int(input('Enter elements in List'))
    list.append(x)
e=int(input('Enter element to be searched'))
pos=0
found=False
while pos<n and not found:
    if list[pos]==e:
        found=True
    else:
        pos+=1
if found:
    print('found')
else:
    print("not found")
