#!/usr/bin/env python
# coding: utf-8

def pa(strp,n,d):
    s=0;
    parr=list(strp.split(","))
    if parr[0]!='':
        for i in parr:
            s=s+int(d[i][n])+pa(d[i][4],n,d)
    return s

def printb(strt,d):
    parr=list(d[strt][4].split(","))
    if parr[0]!='':
        for i in parr:
            printb(i,d)
    if d[strt][3]!=True:
        print(strt)
        d[strt][3]=True
        
def printknapSack(W, wt, val, n, tr,d):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
   
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]+ K[i - 1][w - wt[i - 1]],K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    res = K[n][W]
    print(res)
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        
        if res == K[i - 1][w]:
            continue
        else:
            printb(tr[i-1],d)                    
            res = res - val[i - 1]
            w = w - wt[i - 1]
            
def parse_mempool_csv():
    data = []
    d = {}
    count = -1
    with open('mempool.csv') as f:
        data = f.readlines()
    for line in data:
        count += 1
        if count>0:
            tx_id, fee, weight, parents = line.strip().split(',')
            parents = parents.split(';')
            d[tx_id] = [count, fee, weight, False] + parents
    return d
d = parse_mempool_csv()
f=[]
w=[]
tr=[]
for i in d.values():
    f.append(int(i[1])+pa(i[4],1,d))
    w.append(int(i[2])+pa(i[4],2,d))
    
for i in d.keys():
    tr.append(i)

W=40000
n=len(f)  

printknapSack(W, w, f, n, tr,d)

