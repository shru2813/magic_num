num=int(input())
while (len(str(num)) >1):
    sum=0
    for i in str(num):
        sum+=int(i)
    num=sum
if num==1:
    print('1')
else:
    print('0')