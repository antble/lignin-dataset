package require psfgen
topology /Users/anthonca/Documents/Postdoc/ligningen-project/ligningen/assets/toppar/top_all36_cgenff.rtf
topology /Users/anthonca/Documents/Postdoc/ligningen-project/ligningen/assets/toppar/top_lignin.top
topology /Users/anthonca/Documents/Postdoc/ligningen-project/ligningen/assets/toppar/top_spirodienone.top

resetpsf
segment L {
  residue 1 SYR
  residue 2 SYR
}

patch AO4 L:1 L:2

writepsf L.psf