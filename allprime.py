st=int(input("enter the start:"))
end=int(input("enter the end:"))
for j in range(st,end+1,1):
    p=1
    for i in (2,j,1):
        if(j%i==0):
            p=0
            break
        if(p==1):
            print(j)