#############Crystal Code#######################
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
