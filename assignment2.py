import math
import random
n=0
while 1 :
    n=int(input("Enter a number:"))
    sum=1;
    if n == -1:
        break
    for i in range (1,n+1):
        sum*=i;
    print(n ,"!=" ,sum)