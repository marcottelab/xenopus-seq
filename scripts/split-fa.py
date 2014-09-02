#!/usr/bin/env python
import os
import sys
import gzip

filename_fa = sys.argv[1]
f_fa = open(filename_fa,'r')
if( filename_fa.endswith('.gz') ):
    f_fa = gzip.open(filename_fa,'rb')
filename_base = filename_fa.split('.')[0]

seq_h = ''
seq_list = dict()
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip().lstrip('>')
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append(line.strip())
f_fa.close()

fh_list = dict()
for tmp_h in seq_list.keys():
    tmp_name = 'NA'
    if( tmp_h.startswith('unnamed') ):
        tmp_name = 'unnamed' 
    else:
        tmp_name = tmp_h[0]

    if( not fh_list.has_key(tmp_name) ):
        fh_list[tmp_name] = open('%s.%s.fa'%(filename_base,tmp_name),'w')
    fh_list[tmp_name].write('>%s\n%s\n'%(tmp_h, ''.join(seq_list[tmp_h])))

for tmp_name in fh_list.keys():
    fh_list[tmp_name].close()
