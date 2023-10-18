# Stride to pml 
# This script enables the conversion of STRIDE's secondary structure assignments into a PyMOL-readable format, 
# allowing users to visualize and analyze protein structures with updated secondary structure information
#
# Usage:  
#
# 1- create the .pml file
# python stride-to-pml-vXX.py NameofPdb.pdb
# 
# This will produce two files::
#       1- Stride.update_ss.pml : PyMOL script to update the protein's secondary structure
#       2- NameofPdb.stride : STRIDE's output for further analysis.
#
# 2- launch pymol
# pymol load NameofPdb.pdb,stride Stride.update_ss.pml
# 
# Requirements:
#
# PyMOL: A molecular visualization system. It can be obtained from the official PyMOL website.
# (Schrödinger, LLC 2015)
# STRIDE: A tool for protein secondary structure assignment from atomic coordinates.
# Citation:
# Heinig, M., Frishman, D. (2004). STRIDE: a Web server for secondary structure assignment from known atomic coordinates of proteins. Nucl. Acids Res. , 32, W500-2
#
# Before using the script, ensure that STRIDE and Pymol are installed and accessible from your command line. 
#
# JMB-scripts 2023 with the help of Chat-gpt becaus I'm tanche in python 
#
import sys
import subprocess

def run_stride(pdb_filename, stride_filename):
    cmd = ["stride", pdb_filename]
    try:
        with open(stride_filename, "w") as outfile:
            subprocess.run(cmd, stdout=outfile, check=True)
    except Exception as e:
        print(f"Error running STRIDE: {e}")
        sys.exit(1)

def stride_to_pymol_script(stride_filename, pymol_script_filename):
    try:
        with open(stride_filename, 'r') as infile, open(pymol_script_filename, 'w') as outfile:
            for line in infile:
                if line.startswith("ASG"):
                    chain = line[9]
                    resi = line[11:15].strip()
                    ss = line[24]

                    ss_pymol = {'H': 'H', 'E': 'S', 'T': 'L'}.get(ss, 'L')

                    cmd = f"alter (chain {chain} and resi {resi}), ss='{ss_pymol}'\n"
                    outfile.write(cmd)
    # Append the rebuild command to the end of the PyMOL script
            outfile.write("rebuild\n")
    except Exception as e:
        print(f"Error generating PyMOL script: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py pdb_filename")
        sys.exit(1)

    pdb_filename = sys.argv[1]
    stride_filename = pdb_filename.replace('.pdb', '.stride')
    pymol_script_filename = "Stride.update_ss.pml"

    # Run STRIDE and generate its output file
    run_stride(pdb_filename, stride_filename)

    # Generate the PyMOL script
    stride_to_pymol_script(stride_filename, pymol_script_filename)
    print(f"Generated PyMOL script: {pymol_script_filename}")
