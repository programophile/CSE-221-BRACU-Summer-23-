input_file=open('input1a_1.txt','r')
n,m=map(int,input_file.readline().split())
graph={}
for i in range(n+1):
    graph[i]=[]

for _ in range(m):

    u,v,w=map(int,input_file.readline().split())
    graph[u].append((v,w))
str1=""
for key,value in graph.items():
    str1+=f"{key} : {(' '.join((str(x) for x in value)))}"
    str1+="\n"
output_file=open('output2a_1.txt','w')
output_file.write(str1)