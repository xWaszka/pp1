def f(dice):
    j=0
    d=0
    t=0
    c=0
    p=0
    s=0
    for i in range(0,len(dice)):
        if dice[i] == "1":
            j+=1
        elif dice[i] == "2":
            d+=1
        elif dice[i] == "3":
            t+=1
        elif dice[i] == "4":
            c+=1
        elif dice[i] == "5":
            p+=1
        elif dice[i] == "6":
            s+=1
    if max(j,d,t,c,p,s) == j:
        return 1
    elif max(j,d,t,c,p,s) == d:
        return 2
    elif max(j,d,t,c,p,s) == t:
        return 3
    elif max(j,d,t,c,p,s) == c:
        return 4
    elif max(j,d,t,c,p,s) == p:
        return 5
    elif max(j,d,t,c,p,s) == s:
        return 6
