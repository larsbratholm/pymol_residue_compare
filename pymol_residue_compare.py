import sys
import pymol
import os
import time

pdb1 = sys.argv[1]
pdb2 = sys.argv[2]

# load pdb files
cmd.load(pdb1,"native")
cmd.load(pdb2,"other")

# full path to first pdb file
full_path = os.path.abspath(pdb1)
dir_path = os.path.dirname(full_path)

# parse residue list
reslist = []
sitem = sys.argv[3].split(",")
reslist.extend(sitem[:])

pymol.finish_launching()

# hide initial pdb structures
cmd.do('hide all')
# fit the two files
cmd.do('super native,other')
# set res 1 as center and origin
cmd.do("center native and resi 1")

cmd.do("disable native")
cmd.do("disable other")

cmd.do("cd %s" % dir_path)
for res in reslist:
    # create combined object from native and other
    cmd.do("create %s,native,0,1" % res)
    cmd.do("create %s,other,0,2" % res)
    # coloring
    cmd.do('util.cbap %s' % res)
    # enable all states
    # select 5AA area around specified residue and draw lines
    cmd.do("select %s & (br. all within 5 of (%s and resi %s))" % (res,res,res))
    cmd.do("intra_fit sele")
    cmd.do("show lines, sele")
    # draw sticks for residue
    cmd.do("select %s and resi %s" %(res,res))
    cmd.do("show sticks, sele")
    # center
    cmd.do('set all_states, 1')
    # make sure that all the residue pairs are centered
    cmd.do('pair_fit %s and resi %s and n. ca, native and resi 1 and n. ca' % (res,res))
    cmd.center("%s and resi %s" %(res,res))
    if len(sys.argv) > 4 and sys.argv[4]:
        pymol.cmd.png("%s_%d" % (res,0),width=1200,dpi=1200,quiet=1,ray=1)
        pymol.cmd.rotate("x",90,"%s" % res,camera=0)
        pymol.cmd.png("%s_%d" % (res,1),width=1200,dpi=1200,quiet=1,ray=1)
        pymol.cmd.rotate("y",90,"%s" % res,camera=0)
        pymol.cmd.png("%s_%d" % (res,2),width=1200,dpi=1200,quiet=1,ray=1)
    cmd.disable('%s' %res)
cmd.do("delete sele")
