#############Final Simulation#######################
GlowScript 3.1 VPython
scene.range = 100
#Crystal Code
#list of avgDiffs of each run
avgDiffs = []
angles = []
#bond-length
bl=3.345
#radius of polonium
r=1.45
#lattice size (#of atoms across)
ls=5
#length of each side of lattice in angstroms
len=ls*bl
#list to hold all atoms
atoms = []
for X in range(-len/2,len/2,bl):
    for Y in range(-len/2,len/2,bl):
        for Z in range(-len/2,len/2,bl):
            #create sphere and add to list of atoms
            atoms.append(sphere(pos = vec(X,Y,Z),radius=r,color=color.blue))
#copy of atom list to use after removal of object in reflection code
atomsCopy = atoms[:]

Upper = 24.5
lower = 21
increments = 15
count2 = 0
for b in range(lower,Upper,(Upper-lower)/increments):
    #lam = 1.542
    lam = .8
    #list to hold ending y-values
    Yvals = []
    X = -100
    Xinit = X
    deltaX = .01
    theta = radians(b)
    emitter = box(pos=vec(Xprime(X,theta,0),Yprime(X,theta,0),0),length=len*2, height=len*2, width=.5)
    emitter.rotate(axis=vec(0,1,0),angle=radians(90))
    emitter.rotate(axis=vec(0,0,1),angle=-theta)
    c = curve()
    c.retain = 2000
    for Z in range(-len+bl,len-bl,3):
        for Y in range(-len+bl,len-bl,3):
            #Reflection Code
            X=-100
            #the starting y value
            initY = Yprime(X,theta,Y)
            #incoming wave
            c.append(vec(Xprime(X,theta,Y),Yprime(X,theta,Y),Z)
                ,vec(Xprime(X+deltaX,theta,Y),Yprime(X+deltaX,theta,Y),Z))
            #Wave 1
            while(X < len*2):
                rate(100000)
                #this loop checks for impacts of all spheres
                tmp = vec(Xprime(X,theta,Y),Yprime(X,theta,Y),Z)
                for a in atoms:
                    if(mag(a.pos-tmp) < r):
                        atoms.remove(a)
                        newWave(X,vec(tmp.x-Xprime2(X,theta,Y)
                            ,tmp.y-Yprime2(X,theta,Y),0),theta,Y)
                X=X+deltaX
                c.append(tmp)
            c.clear()
            atoms = atomsCopy[:]
    avgDiffs.append(1/avgDiff(Yvals))
    Yvals.clear()
    angles.append(b)
    emitter.visible=False
    count2 = count2 + 1
    print(count2)
#graphing code
f1 = gcurve(color=color.green)
dat2 = 10
for i in range(0,11):
    f1.plot(angles[i],avgDiffs[i])

#These functions calculate sinusoidal wave with the axes rotated
#wave 1
def Xprime(X,theta,Y):
    return X*cos(-theta)-(Y+cos(((2*pi)/lam)*X))*sin(-theta)
    
def Yprime(X,theta,Y):
    return X*sin(-theta)+(Y+cos(((2*pi)/lam)*X))*cos(-theta)
    
def Xprime2(X,theta,Y):
    return X*cos(theta)-(Y+cos(((2*pi)/lam)*X))*sin(theta)
    
def Yprime2(X,theta,Y):
    return X*sin(theta)+(Y+cos(((2*pi)/lam)*X))*cos(theta)

#reflected wave
def newWave(X,diff,theta,Y):
    deltaX = .01
    c2 = curve(vec(Xprime(X,theta,Y)
        ,Yprime(X,theta,Y),Z),vec(Xprime(X+deltaX,theta,Y)
        ,Yprime(X+deltaX,theta,Y),Z))
    c2.retain = 2000
    while(X < -Xinit):
        rate(100000)
        X=X+deltaX
        tmp = vec(Xprime2(X,theta,Y),Yprime2(X,theta,Y),Z)
        diff2 = vec(Xprime(X,theta,Y)-tmp.x,Yprime(X,theta,Y)-tmp.y,0)
        c2.append(tmp+diff)
    c2.clear()
    Yvals.append(Y+cos(((2*pi)/lam)*X))
    
#average difference
def avgDiff(list):
    sum = 0
    count = 0
    for i in range(list.length):
        for j in range(i+1,list.length):
            sum=sum+abs(list[i]-list[j])
            count=count+1
    return sum/count
