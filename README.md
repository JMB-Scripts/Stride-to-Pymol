## Stride to pml 
This script enables the conversion of STRIDE's secondary structure assignments into a PyMOL-readable format, 
allowing users to visualize and analyze protein structures with updated secondary structure information
#
## Usage:  

1- create the .pml file

'bash python stride-to-pml-vXX.py NameofPdb.pdb'

This will produce two files::
      1- Stride.update_ss.pml : PyMOL script to update the protein's secondary structure
      2- NameofPdb.stride : STRIDE's output for further analysis.

2- launch pymol

'bash pymol NameofPdb.pdb Stride.update_ss.pml'
 
## Requirements:
PyMOL: A molecular visualization system. It can be obtained from the official PyMOL website.
(Schrödinger, LLC 2015)
STRIDE: A tool for protein secondary structure assignment from atomic coordinates.
Citation:
Heinig, M., Frishman, D. (2004). STRIDE: a Web server for secondary structure assignment from known atomic coordinates of proteins. Nucl. Acids Res. , 32, W500-2

Before using the script, ensure that STRIDE and Pymol are installed and accessible from your command line. 
