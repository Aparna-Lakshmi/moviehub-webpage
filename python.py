n=int(input())
l1=list(map(int,input().split(" ",n-1)))
x=len(l1)
sum1=0
while(n!=0):
    if(x>4):
        sum1=sum1+(l1[0]*l1[1]*l1[2])
    elif(x>3):
        sum1=sum1+(l1[0]*l1[1])
    elif(x>2):
        sum1=sum1+(l1[0])
    if(x>1):
        l1.remove(l1[1])
    elif(x==1):
        l1.emove(l1[0])
    x=len(l1)
print(sum1)
    



    