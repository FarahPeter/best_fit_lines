import matplotlib.pyplot as plt
import numpy as np
import math
#Lines of best fit:



#Linear line of best fit:
#y=ax+b
def LinearLineOfBestFit(L,D):#(y,x)
    try:
        l=len(L)
        AverageOfL=0
        AverageOfD=0
        for i in range (l):
            AverageOfL=AverageOfL+L[i]
            AverageOfD=AverageOfD+D[i]
        AverageOfL=AverageOfL/l
        AverageOfD=AverageOfD/l
        
        
        ANumerator=0
        ADenomenator=0
        for i in range (l):
            ANumerator=ANumerator+((L[i]-AverageOfL)*(D[i]-AverageOfD))
            ADenomenator=ADenomenator+(D[i]-AverageOfD)**2
        a=ANumerator/ADenomenator
        b=AverageOfL-a*AverageOfD
        return ([a,b])
    except ZeroDivisionError:
        print("Line estimate for one point is not definned")
    

#Exponential line of best fit:
#y=Ar^x  (y=L and x=D)
def ExponentialLineOfBestFit(L,D):
    C=[np.log10(L[i]) for i in range (len(L))]
    Tr=LinearLineOfBestFit(C,D)
    r=10**Tr[0]
    A=10**Tr[1]
    return([A,r])



#Quadratic Regression
#y=ax^2 + bx + c
def QuadraticLineOfBestFit(L,D):
    n=len(L)
    sumX=0
    sumY=0
    sumX2=0
    sumX3=0
    sumX4=0
    sumXY=0
    sumX2Y=0
    for i in range (n):
        sumX=sumX+D[i]
        sumY=sumY+L[i]
        sumX2=sumX2+(D[i])**2
        sumX3=sumX3+(D[i])**3
        sumX4=sumX4+(D[i])**4
        sumXY=sumXY+L[i]*D[i]
        sumX2Y=sumX2Y+((D[i])**2)*L[i]
    a=(((sumX2Y-(sumX2*sumY)/n)*((sumX2)-((sumX)**2)/n))-(((sumXY)-(sumX*sumY)/n)*((sumX3-(sumX2*sumX)/n))))/((((sumX2)-((sumX)**2)/n)*(sumX4-((sumX2)**2)/n))-((sumX3-(sumX2*sumX)/n)**2))
    b=((((sumXY)-(sumX*sumY)/n)*(sumX4-((sumX2)**2)/n))-((sumX2Y-(sumX2*sumY)/n)*(sumX3-(sumX2*sumX)/n)))/((((sumX2)-((sumX)**2)/n)*(sumX4-((sumX2)**2)/n))-((sumX3-(sumX2*sumX)/n)**2))
    c=(sumY/n)-(b*sumX/n)-(a*sumX2/n)
    return([a,b,c])


#Curve fit
#the Higher X is the more smooth the fitted curve will be but more information will be lost
def EveryXLineOfBestFit(L,D,X):
    l=len(L)
    tot=[0]*l
    for i in range (0,l-X+1,X):
        x=[j for j in range (i,i+X)]
        y=[L[j] for j in range (i,i+X)]
        ITlinLineOfBestFit=LinearLineOfBestFit(y,x)
        for j in range (i,i+X):
            tot[j]=ITlinLineOfBestFit[0]*D[j]+ITlinLineOfBestFit[1] 
    remL=math.ceil((l/X - int(l/X))*X)
    if (remL>1):
        tempY=[L[i] for i in range (l-1-remL,l)]
        tempX=[D[i] for i in range (l-1-remL,l)]
        LastITlinLineOfBestFit=LinearLineOfBestFit(tempY,tempX)
        for i in range (l-1,l-2-remL,-1):
            tot[i]=LastITlinLineOfBestFit[0]*D[i]+LastITlinLineOfBestFit[1]    
    elif(remL==1):
        tot[l-1]=L[l-1]
    return(tot)











#test case for exponential
y=[2,4,8,16,32]
x=[1,2,3,4,5]
a=ExponentialLineOfBestFit(y,x)
z=[0,0,0,0,0]
for i in range (len(y)):
    z[i]=a[0]*(a[1]**x[i])
plt.figure(1)
plt.plot(x,y,"b")
plt.plot(x,z,"r")
plt.xlabel('X')
plt.ylabel('Y')


#test case for quadratique
xx=[0.03825,0.17725,0.309792]
yy=[8.08382,8.51159,9.09944]
aa=QuadraticLineOfBestFit(yy,xx)
zz=[0,0,0]
for i in range (len(yy)):
    zz[i]=aa[0]*xx[i]**2+aa[1]*xx[i]+aa[2]
plt.figure(2)
plt.plot(xx,yy,"b")
plt.plot(xx,zz,"r")
plt.xlabel('X')
plt.ylabel('Y')


#test case for curve fit
xxx=[1,2,3,4,5,6,7,8,9]
yyy=[54,58,56,35,98,68,75,85,95]
aaa=EveryXLineOfBestFit(yyy,xxx,4)
plt.figure(3)
plt.plot(xxx,yyy,"b")
plt.plot(xxx,aaa,"r")
plt.xlabel('X')
plt.ylabel('Y')