#!/usr/bin/python
# binary to text
# read b_degree.bin b_adj.bin
# output
#       edges.csv:      each edge for gephi
#       adj.txt:        neighbor for each node
import struct

fdeg = open("b_degree.bin", 'rb')
fadj = open("b_adj.bin", 'rb')

fedges_csv = open("edges.csv","w")
fadj_txt = open("adj.txt", "w")

buf = fdeg.read(4)
int_len, = struct.unpack("i", buf)

buf = fdeg.read(4)
num_of_nodes, = struct.unpack("i", buf)

buf = fdeg.read(4)
lines, =  struct.unpack("i", buf)

#print int_len, num_of_nodes, lines
degs = []
for i in range(0, num_of_nodes):
    buf = fdeg.read(4)
    deg, = struct.unpack("i", buf)
    degs.append(deg)

fdeg.close()

#print sum(degs)
edges = []
bi_edges = []
for i in range(0, num_of_nodes):
    for j in range(0, degs[i]):
        buf = fadj.read(4)
        end, = struct.unpack("i", buf)
        if i < end:
            edges.append((i, end))
        bi_edges.append((i, end))

fadj.close()

oa = -1

for a, b in bi_edges:
    if a != oa:
        if oa != -1:
            fadj_txt.write('\n')

        oa = a

        fadj_txt.write((str)(b) + ' ')
    else:
        fadj_txt.write((str)(b) + ' ')

#for i in edges:
#    print i

for i in edges:
    a, b = i
    fedges_csv.write((str)(a) + "\t" + (str)(b) + "\n")
