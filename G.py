from collections import defaultdict, deque
first = input().split(" ")
endNode = int(first[0])
M = int(first[1])
edges = defaultdict(list)
visitedEdges = {1}
for i in range(M):
    line = input().split(" ")
    edges[int(line[0])].append(int(line[1]))
    edges[int(line[1])].append(int(line[0]))
q = deque(edges[1])
def bfs():
    ans = 0
    while q:
        qLen = len(q)
        for _ in range(qLen):
            point = q.popleft()
            if point == endNode:
                return ans
            visitedEdges.add(point)
            for e in edges[point]:
                if e not in visitedEdges:
                    q.append(e)
        ans += 1
    return -1
print(bfs())