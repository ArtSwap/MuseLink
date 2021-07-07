#!/usr/bin/env python
"""Usage: python setup.py(argmodel,arnlist,argfactor,argdirname)
Remember this system is meant for use in a conda enviroment or something else separate from your main system, as it installs old versions of some packages such as Pytorch. It could break other things on your computer if you use the packages for anything else""" #but then again, if you're looking in here and using it this way, you probably know that already.

import argparse, os
from git import Repo

# Setup code
def main(args):
    #adds open-source GAN packages. only really use the Generator module, could make a new one as an optimization but right now I can't test this code, so no experimenting.
    Repo.clone_from("https://github.com/CurtisASmith/stylegan2-pytorch","stylegan2-pytorch")
    os.chdir("stylegan2-pytorch")
    # sets enviroment variables according to arguments
    os.environ("MODEL") = argmodel
    os.environ("NLIST") = argnlist
    os.environ("FACTOR") = argfactor
    os.environ("DIRNAME") = argdirname

# Standard boilerplate to call the main() function to begin the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Use this script to set up the environment for the tool scripts. Syntax: python setup.py(argmodel,arnlist,argfactor,argdirname)",
        fromfile_prefix_chars = '@' )
    # Parameters:
    parser.add_argument(
        "argmodel",
        help = "Usage: -argmodel <path_to_model>",
        default = "./models/paray-512px.pt")
    
    parser.add_argument(
        "argnlist",
        help = "Usage: -argnlist <path_to_nlist>",
        default = "./models/nlist.db")
    
    parser.add_argument(
        "argfactor",
        help = "Usage: -argfactor <path_to_factor>",
        default = "./models/factor.pt")

    parser.add_argument(
        "argdirname",
        help = "Usage: <dir_latentexplore>",
        default = "./latentexplore/")
    
    args = parser.parse_args()
    main(args)