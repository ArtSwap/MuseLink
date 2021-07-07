#!/usr/bin/env python
# Usage: python setup.py(argmodel,arnlist,argfactor,argdirname)

import argparse, os, time
import modules

# Gather our code in a main() function
def main(args):
    model = os.getenv("MODEL")
    explore = exp
    p_num = argnum
    t_a, t_b = argta, argtb
    norm = argnorm
    savename = os.getenv("DIRNAME") + strftime("%Y-%d%b-%H%M-%S",localtime())
    factor = os.getenv("FACTOR")
    vec = argvec
    scale = argscale
    if !explore:
        print("Running the Paray Painter Program...")
        paray_gen(model,p_num,t_a,t_b,norm)
    if explore:
        print('Running the Experimental Latent Explorer...')
        gen_factor(savename,factor,vec,scale)
        
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description = "Paray Painter CLI | Usage: Regular generation runs can be modified with -argnum for p_num, -argta -argtb for truncation floats, -argnorm True or False | for explorer, use -exp True, -argvec and -argscale. See documentation.",
        fromfile_prefix_chars = '@' )
    # Parameters:    
    parser.add_argument(
        "exp",
        help = "Usage: -argnlist <path_to_nlist>",
        default = False)

    parser.add_argument(
        "argnum",
        help = "num of painter generations",
        default = 10 )

    parser.add_argument(
        "argta",
        help = "truncation a" ,
        default = "0.45" )
    
    parser.add_argument(
        "argtb",
        help = "truncation b",
        default = "0.6" )
    
    parser.add_argument(
        "argnorm",
        help = "Normalize?",
        default = "True")
    
    parser.add_argument(
        "argvec",
        help = "Vector for exploration",
        default = 1)

    parser.add_argument(
        "argscale",
        help = "Scalar for exploration",
        default = 7)
    
    args = parser.parse_args()
    main(args)