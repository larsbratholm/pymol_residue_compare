# ProCS15
To open overlayed environments (residues within 5Å) from residue 31 and 35 from structures pdb1.pdb and pdb2.pdb run
`pymol -r pymol_residue_compare.py -- example/pdb1.pdb example/pdb2.pdb 31,35`

To generate png files automatically from 3 different angles, add `1` or `True` as a final argument

`pymol -r pymol_residue_compare.py -- example/pdb1.pdb example/pdb2.pdb 31,35 True`

![Residue 31](https://github.com/larsbratholm/pymol_residue_compare/example/31_0.png)
![Residue 35](https://github.com/larsbratholm/pymol_residue_compare/example/35_1.png)


