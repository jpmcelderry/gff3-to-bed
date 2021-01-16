#!/usr/bin/env python

import sys

def main(args):
    
    for arg in args:
        input_file = open(arg,"r")
        outputname = arg.split(".gff")[0]
        output_file = open(outputname +".bed" ,"x")

        for line in input_file:
            if line[0] != '#':
                fields = line.split('\t')
                name = fields[8].split("Name=")
                if len(name)>=2:
                    name = name[1].split(';')[0].strip('\t\n')
                else:
                    name = "."
                output_file.write(fields[0] + '\t' + fields[3] + '\t' + fields[4] + '\t' + name + '\t' + fields[5] + '\t' + fields[6] + '\t' + '\n')
        
if __name__ == "__main__":
    main(sys.argv[1:])