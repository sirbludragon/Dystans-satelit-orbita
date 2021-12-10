import math
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

xlist=[]
ylist=[]
distance=[]
time=[]

x1list=[]
y1list=[]
distance1=[]
time1=[]

Bdis=[]

kerbin = ['kerbin', 5.2915158 * pow(10, 22), 600000, 5.98594444444, 70000, 13599840256, 2863330, 426.090046296, 'planet', '#1F618D', 1.7565459 * pow(10, 28)]
G=6.67408*(10**-11)

apogee=300000
perigee=100000
a=(apogee+perigee+2*kerbin[2])/2
b=((apogee+kerbin[2])*(perigee+kerbin[2]))**0.5
E=(apogee-perigee)/(apogee+kerbin[2]+perigee+kerbin[2]) #To samo dokładniejsze chyba
va=((2*G*kerbin[1]/(apogee+kerbin[2]))-(G*kerbin[1]/a))**0.5
vp=((2*G*kerbin[1]/(perigee+kerbin[2]))-(G*kerbin[1]/a))**0.5
T=2*math.pi*(((a**3)/(G*kerbin[1]))**0.5)
print(a*math.cos(0))
t=0

apogee1=839841 #1239841
perigee1=100000
a1=(apogee1+perigee1+2*kerbin[2])/2
b1=((apogee1+kerbin[2])*(perigee1+kerbin[2]))**0.5
T1=2*math.pi*(((a1**3)/(G*kerbin[1]))**0.5)
print((round(T1,3)*100)/(round(T,3)*100))
t1=0

while t<36*((round(T1,3)*100)/(round(T,3)*100))*math.pi:
    x=a*math.cos(t-(math.pi/3))-(a-kerbin[2]-perigee) ##dodanie Pi/4 do sin i cos
    y=b*math.sin(t-(math.pi/3))
    xlist.append(x)
    ylist.append(y)
    d=(((x-perigee)**2+y**2)**0.5)-kerbin[2]
    distance.append(d)
    time.append(t*round(T,3)/(2*math.pi))
    t+=1/round(T,3)

while t1<36*math.pi:
    x1 = a1 * math.cos(t1)-(a1-kerbin[2]-perigee1)
    y1 = b1 * math.sin(t1)
    x1list.append(x1)
    y1list.append(y1)
    d1 = (((x1-perigee) ** 2 + y1 ** 2) ** 0.5)-kerbin[2]
    distance1.append(d1)
    time1.append(t1*round(T1,3)/(2*math.pi))
    t1 += 1/round(T1,3)

n=0
print(t1)
while n<len(xlist):
    dis=(((xlist[n])-(x1list[n]))**2+((ylist[n])-(y1list[n]))**2)**0.5
    Bdis.append(dis)
    n += 1

circle3 = plt.Circle((0,0), 600000, fill=True)
ax = plt.subplot(212, aspect='equal')
ax.add_artist(circle3)
plt.plot(xlist,ylist)
plt.plot(x1list,y1list)
plt.plot(xlist[0],ylist[0],"*",color="purple")
plt.plot(x1list[0],y1list[0],"*",color="red")

minValue=min(Bdis)
minValueIndex=Bdis.index(minValue)
minValueIndexValue=(minValueIndex/(2*math.pi))
plt.plot(xlist[round((minValueIndexValue/time[-1])*(len(xlist)))],ylist[round((minValueIndexValue/time[-1])*(len(ylist)))],".",color="purple")
plt.plot(x1list[round((minValueIndexValue/time[-1])*(len(x1list)))],y1list[round((minValueIndexValue/time[-1])*(len(y1list)))],".",color="red")
print(minValueIndexValue)

plt.subplot(221)
plt.plot(time,distance)
plt.plot(time1,distance1)

plt.subplot(222)
plt.plot(time1,Bdis)
plt.show()

print(round(T,3),round(T1,3))
print(len(xlist),len(x1list))
print(a1,b1,)

