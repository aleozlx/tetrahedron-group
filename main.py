import numpy as np

a = np.arange(4)
u = lambda x: x[[0, 2, 3, 1]]
v = lambda x: x[[3, 1, 0, 2]]
y = lambda x: x[[1, 3, 2, 0]]
z = lambda x: x[[2, 0, 1, 3]]
print(u(a))

def dfs(G, a = None):
    visited = np.zeros_like(G).astype(bool)
    predecessors = -np.ones_like(G)
    stack = [a]
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            if G[u]:
                discovered = np.array([[v, next(counter)] for v in G[u] if not visited[v]])
                stack.extend(reversed(discovered[:, 0]))
                predecessors[discovered[:, 0]] = u
    return predecessors
