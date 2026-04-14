mol load psf L.psf
mol addfile minimize.coor
set sel [atomselect top all]
$sel writepdb minimized_wrapped.pdb
mol delete all
exit
