#-*-coding: utf-8-*-
from queue import Queue

maze = []

print("input:")
for i in range(0,6):
    w=input().split()
    maze.append(w)
print(maze)
d = [[-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1],
     [-1,-1,-1,-1,-1,-1]]

start_point=[0,0]
sx=0
sy=0
ex=5
ey=5
dx = [ 1,0,-1,0 ]
dy = [ 0,1,0,-1 ]
q = Queue()

def bfs():
    point=[0,0]
    d[sx][sy] = 0 
    q.put(point)
    while not q.empty():
        p=q.get()
        if(p[0]==ex and p[1]==ey):
            break
        for i in range(0,4):
            nx = p[0]+dx[i]
            ny = p[1]+dy[i]
            if(0<=nx and nx<6 and ny>=0 and ny<6 and maze[nx][ny]!='#' and d[nx][ny]== -1):
                point=[nx,ny]
                q.put(point)
                d[nx][ny]=d[p[0]][p[1]]+1
    return d[ex][ey]

g=bfs()
print("最短步数：")
print(g)

