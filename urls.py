#!/usr/bin/python3

import sys
import os


infile = sys.argv[1]
spec = sys.argv[2]
outfile = sys.argv[3]

with open('/home/zero/opmm.txt','rt') as ffile:
    with open('{}'.format(infile),'wt') as fout:
        for line in ffile:
            fout.write(line.replace('https://','http://').replace('/,','/\n,'))

os.system('cat {} | grep -v blogspot | grep -v weevly | grep {} > {}.txt'.format(infile,spec,outfile))


