a=int(input())
b=int(input())
f=open('PassBase.txt','w')
for i in range(10**a):
    print(str(i).zfill(b))
    
    f.write(str(i).zfill(b)+'\n')
f.close()
#for i reverse(range())
