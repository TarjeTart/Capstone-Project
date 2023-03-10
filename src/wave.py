#############Wave Code#######################
#X and Y prime are for outgoing wave
def Xprime(X,theta,Y):
    return X*cos(-theta)-(Y+cos(((2*pi)/lam)*X))*sin(-theta)
    
def Yprime(X,theta,Y):
    return X*sin(-theta)+(Y+cos(((2*pi)/lam)*X))*cos(-theta)

#X and Y prime2 are for reflected waves    
def Xprime2(X,theta,Y):
    return X*cos(theta)-(Y+cos(((2*pi)/lam)*X))*sin(theta)
    
def Yprime2(X,theta,Y):
    return X*sin(theta)+(Y+cos(((2*pi)/lam)*X))*cos(theta)
