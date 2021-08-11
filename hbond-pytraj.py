import warnings

# use pytraj
import pytraj as pt

# load trajectory from file
traj = pt.iterload('RBD-Helix.NoWAT.mdcrd.nc', 'NoW.RBD-Helix.rec.wat.leap.prmtop')     ### Change File name

dataHB = pt.search_hbonds(traj)

print(dataHB.donor_acceptor)

f = open("InterMolHB-Pairs.txt","r")
HBpairs = [m.replace('_','').replace('@','_').strip() for m in f.readlines()[1:]]

print(HBpairs)

h_values = dataHB.data[HBpairs].values
print(sum(h_values))

with open('Total-HBonds-RBD-Helix.txt','w') as f:
    for item in range(0,len(sum(h_values))):
        print(item,sum(h_values)[item], file = f)




