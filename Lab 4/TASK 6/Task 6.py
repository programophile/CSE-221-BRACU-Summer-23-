def dfs(mattrix,r,c):
    if r < 0 or r >= len(mattrix) or c < 0 or c >= len(mattrix[0]) or mattrix[r][c] == '#' :
        return 0
    diamond=0
    if mattrix[r][c]=="D":
        diamond+=1
    mattrix[r][c]="#"
    diamond+=dfs(mattrix,r+1,c)
    diamond+=dfs(mattrix,r-1,c)
    diamond+=dfs(mattrix,r,c+1)
    diamond+=dfs(mattrix,r,c-1)
    return diamond


def max_diamond(r,c,str1):
    rows=str1.strip().split("\n")
    mattrix=[list(i) for i in rows]
    diamonds=0
    for r in range(r):
        for c in range(c):
            if mattrix[r][c]=="D":
                diamonds=max(diamonds,dfs(mattrix,r,c))
    return diamonds
input_file=open('input6_1.txt','r')
r,c=map(int, input_file.readline().split())
mattrix=""
for i in range(r):
    mattrix+=input_file.readline()
# print(mattrix)

a=max_diamond(r,c,mattrix)
output_file=open('output6_1.txt','w')
output_file.write(str(a))
