import sys
###Max fun of arrays

xy = input().split(' ')
xy=int(xy[0])

##tme=input().split(' ')
##print(tme)
#print(xy)
#print(x)

def conv_min(Tt):
    our_scale= 24*60
    addr = 0 
    if Tt[2] == "PM":
        addr = 12*60
    if Tt[0]==12:
        Tt[0] =0
    
    return  ((60*Tt[0])+(Tt[1]) + addr)

def myf(a,t):
    ts= [0]*3
    ts[0]= t[0].split(":")
    #print("the ts[0] is" + str(ts[0]))
    
    ts[0],ts[1]=int(ts[0][0]),int(ts[0][1])
    ts[2]= t[1]
    
    T = conv_min(ts)
    #print(ts)
    p= conv_min(a[0:3])
    q= conv_min(a[3:6])
    #print(T,p,q)
    if p>q:
        if T > q and T < p:
            return False
        else:
            return True
    
    if T>=p and q >=T :
        return True
    return False
    
    


def new_para():
    soln= ""
    temp=0
    tme=input().split(' ')
    # tme ek list h with ["HH:MM","AM/PM"]
    #print("our time = "+ str(tme))
    x = input().split(' ')
    x=int(x[0])
    #print("this")
    #print(x)
    b=[0]*x
    for _ in range(x):
        b[_]=input().split(' ')
        
    #print(b)
    # yaha b ek list h [time 1, am/pm,time2,am/pm]
    
    c= [0]*x
    for Q in range(x):
        c[Q]=[0]*6
        c[Q][0]= b[Q][0].split(":")
        c[Q][0],c[Q][1]=int(c[Q][0][0]) ,int(c[Q][0][1])
        c[Q][2]= b[Q][1]
        c[Q][3]= b[Q][2].split(":")
        c[Q][3],c[Q][4]=int(c[Q][3][0]) ,int(c[Q][3][1])
        c[Q][5]= b[Q][3]
    #for tt in range(x):
        #temp = d[tt]
    # c me x time input le rakhe h for each time range apne ko batane ka h kya time match ho rha kahi se 
    
    for li in range(x):
        if myf(c[li],tme):
            soln = soln +"1"
        else:
            soln += "0"
    
    print(soln)
    
    
    
    
    return
    ##yaha c jo h vhi h apna array 
    
    
for ijk in range(xy):
    new_para()
