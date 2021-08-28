from array import *

def interclasare(x, l, m, r,a):
    i=l
    j=m+1
    k=l
    while i <= m and j <= r:
        if x[i] < x[j]:
            a[k] = x[i]
            i += 1
        else:
            a[k] = x[j]
            j += 1
        k += 1
    while i <= m:
        a[k] = x[i]
        i += 1
        k += 1
    while j <= r:
        a[k] = x[j]
        j += 1
        k += 1
    for h in range(l,r+1):
        x[h] = a[h]


def merge_sort(x,l,r,a):
    if l < r:
        m= l + ( r - l )//2
        merge_sort(x, l, m, a)
        merge_sort(x, m+1, r, a)  
        interclasare(x, l, m, r, a) 

n=int(input("Lungimea vectorului"))
x=array('i',[])
a=array('i',[])
for i in range(0,n):
    k = int(input())
    x.append(k)
for i in range(0,n):
    a.append(x[i])
print(x)
merge_sort(x, 0, (n - 1), a)  
print(x)
