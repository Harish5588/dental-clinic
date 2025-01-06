# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

def fab(n):
    s=[]
    a,b=0,1
    for i in range(n):
        s.append(a)
        a,b=b,a+b
    return s
print(fab(10))