#!/usr/bin/python
# text to binary
# read  gephi_edges.csv: each edge for gephi
# output
#       b_degree.bin b_adj.bin

import struct

fin = open("edges.csv")
fout = open("b_degree.bin", 'wb')
fadj = open("b_adj.bin", 'wb')

edges = []
count = [0]*10
lines = fin.readlines()
for line in lines:
    s,t = line.split()
    count[(int)(s)] += 1
    count[(int)(t)] += 1
    edges.append((s,t))
    edges.append((t,s))


#print sys.getsizeof(int())

fout.write(struct.pack("i", 4))
fout.write(struct.pack("i", len(count)))
fout.write(struct.pack("i", len(lines) * 2))
#fout.write(struct.pack("i", len(lines)))

for node in count:
    fout.write(struct.pack("i", node))
    #print node

edges.sort()

for edge in edges:
    fadj.write(struct.pack("i", int(edge[1])))
    #print edge[0], edge[1]
