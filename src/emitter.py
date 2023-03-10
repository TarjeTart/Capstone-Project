#############Reflection Code#######################
#list to hold ending y-values
        Yvals = []
        for Z in range(-len+bl,len-bl,3):
            for Y in range(-len+bl,len-bl,3):
                #Reflection Code
                theta = radians(b)
                #initial x value (not rotated)
                X = -100
                Xinit = X
                #change in x
                deltaX = .01
                #the starting y value
                initY = Yprime(X,theta,Y)
                #create emitter plate
                emitter = box(pos=vec(Xprime(X,theta,0)
                    ,Yprime(X,theta,0),0),length=len*2, height=len*2, width=.5)
                emitter.rotate(axis=vec(0,1,0),angle=radians(90))
                emitter.rotate(axis=vec(0,0,1),angle=-theta)
                #incoming wave
                c = curve(vec(Xprime(X,theta,Y),Yprime(X,theta,Y),Z)
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
                c.visible = False
                del c
                atoms = atomsCopy[:]
        print(b + " theta, " + lam + " lambda: " + avgDiff(Yvals))
        emitter.visible = False
        del emitter
