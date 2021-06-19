#!/usr/bin/env python
# coding: utf-8

import operator

def pa(strp,n,d):
    s=0;
    parr=list(strp.split(","))
    if parr[0]!='':
        for i in parr:
            s=s+int(d[i][n])+pa(d[i][4],n,d)
    return s

def printb(strt,d):
    file1 = open("block.txt","a")
    parr=list(d[strt][4].split(","))
    if parr[0]!='':
        for i in parr:
            printb(i,d)
    if d[strt][3]!=True:
        file1.write(strt)
        file1.write("\n")
        print(strt)
        d[strt][3]=True
        
def selc(d,n,w,tr):
    s,f,c=0,0,0   
    f1= open("fee_obtained.txt","a")
    f2= open("weight_obtained.txt","a")
    for i in d.values():
        
        if(s+i[2]<=w):
            s=s+int(i[2])
            f=f+int(i[1])
            printb(tr[c],d)
        c=c+1
    print(f)
    f1.write(str(f))
    print(s)
    f2.write(str(s))
        
def parse_mempool_csv():
    data = []
    d = {}
    count = -1
    ratios=0.0
    with open('mempool.csv') as f:
        data = f.readlines()
    for line in data:
        count += 1
        if count>0:
            tx_id, fee, weight, parents = line.strip().split(',')
            parents = parents.split(';')
            d[tx_id] = [ratios, fee, weight, False] + parents
    return d

d = parse_mempool_csv()
for i in d.values():
    i[1]=int(i[1])+pa(i[4],1,d)
    i[2]=int(i[2])+pa(i[4],2,d)
    i[0]=float(i[1]/i[2])
    
d = dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
W=4000000
n=len(d)
tr=[]
for i in d:
    tr.append(i)
selc(d,n,W,tr)

