
from functools import reduce

slist =[1,2,3,4,5,6]
def sum_ele(a):
    m=0
    for i in range(len(a)):
        m+=a[i]
    return m
print(sum_ele(slist))   
print(list(map(lambda x:x*x,slist)))
print(list(filter(lambda val:val%3!=0,slist)))
print(reduce(lambda x,y:x+y,slist))
print(reduce(lambda x, y: x * y, slist))
xlist = [["xyz",1],["abc",2],["pqr",3]]
print(list(sorted(xlist,key=lambda x:x[1])))
print(list(sorted(xlist,key=lambda x:x[0],reverse=True))) 