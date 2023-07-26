
import numpy as np
# n=int(input())
# m=int(input())
input_file=open('input1a_2.txt','r')
n,m=map(int,input_file.readline().split())
mattrix=np.zeros((n+1,n+1))
for _ in range(m):
  u,v,w=map(int,input_file.readline().split())
  mattrix[u][v]=w

output_file=open('output1a_2.txt','w')
str1=""
for i in mattrix:
  str1+=" ".join(str(int(x)) for x in i)
  str1+="\n"
output_file.write(str1)
output_file.close()