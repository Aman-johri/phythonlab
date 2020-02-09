import math
a=int(input())
b=int(input())
c=int(input())
d=b*b-4*a*c
if d<0:
    print("roots are imaginary")
elif d>0:
    x1=-b+(math.sqrt(d))/2*a
    x2=-b-(math.sqrt(d))/2*a
    print("roots are real")
    print(x1)
    print(x2)
    
