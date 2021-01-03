# 백준 1260 신지원

def DFS(V):
    global Edges, mark_DFS
    mark_DFS[V] = True
    print(V,end = " ")
    for i in Edges[V]:
        if mark_DFS[i] != True:
            DFS(i)
    
def BFS(V):
    global Edges, mark_BFS
    Queue= []
    Queue.append(V)
    while Queue:
        node = Queue.pop(0)
        if mark_BFS[node] != True:
            mark_BFS[node] = True
            print(node, end = " ")
            for i in Edges[node]:
                Queue.append(i)
    
N, M, V = map(int, input().split())
Edges = [[]for i in range(N+1)]
for i in range(M):
    v1, v2 = map(int, input().split())
    Edges[v1].append(v2)
    Edges[v2].append(v1)
for i in range(len(Edges)):
    Edges[i] = sorted(Edges[i])

mark_DFS = [False]*(N+1)
DFS(V)
print()

mark_BFS = [False]*(N+1)
BFS(V)