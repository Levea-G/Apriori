scale=50
cfm=scale*8
lines=scale*1000
def dfs(inter,st,ct,items):
    vec1[8-ct].append(items)
    if ct==0:return
    for i in range(st,len(vec)):
        temp=inter.intersection(vec[i])
        if len(temp)<cfm:continue
        tmp=items.copy()
        tmp.add(i)
        dfs(temp,i+1,ct-1,tmp)
xx=open('T1014D%dK.dat'%scale,'r')
vec=[set() for _ in range(1000)]
for item,i in zip(xx.readlines(),range(lines)):
    item=item.strip().split()
    for num in item:
        vec[int(num)].add(i)
xx.close()
vec1=[[] for _ in range(8)]
dfs(set(range(lines)),0,8,set())
vec1.pop(0)
for item in vec1:
    l=len(item)
    if l==0:break
    print(l)
    for i in range(min(5,len(item))):
        print(item[i])