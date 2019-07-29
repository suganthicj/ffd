def solution(x11):     
    if len(x11) == 1:
         return x11[0]
    x11 = sorted(x11)
    for p in range(0 , len (x11) , 2):
         if p+1 == len(x11):
             return x11[p]
         if x11[p] != x11[p+1]:
             return x11[p]
