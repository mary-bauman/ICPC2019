from collections import defaultdict, deque
from time import time
t1 = time()
first = input().split(" ")
endNode = int(first[0])
M = int(first[1])
edges = defaultdict(list)
visitedEdges = {1}
for i in range(M):
    line = input().split(" ")
    edges[int(line[0])].append(int(line[1]))
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
print(bfs())

time = "{:.6f}".format(time() - t1)
print(f"time = {time}")







# from collections import deque
# # from time import time
# # t1 = time()
# first = input().split(" ")
# endNode = int(first[0])
# M = int(first[1])
# edges = []
# visitedEdges = set()
# for i in range(M):
#     line = input().split(" ")
#     edges.append((int(line[0]), int(line[1])))
# q = deque()
# for s, e in edges:
#     if s == 1:
#         q.append(e)
# def bfs():
#     ans = 0
#     while q:
#         qLen = len(q)
#         for _ in range(qLen):
#             point = q.popleft()
#             if point == endNode:
#                 return ans
#             visitedEdges.add(point)
#             for s, e in edges:
#                 if e not in visitedEdges and s == point:
#                     q.append(e)
#         ans += 1
# print(bfs())
