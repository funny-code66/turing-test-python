con = [
  [2, 3, 4],
  [5, 6],
  [],
  [7, 8],
  [9, 10],
  [],
  [11, 12],
  [],
  [],
  [],
  [],
  [],
]

def dfs(G, s):
  """ G: graph, s: root node, q: queue, P={s:None}: parent """
  visited = set()
  Q=[s]; print(s)
  while Q:
    u = Q.pop()
    if u in visited: continue
    visited.add(u)
    print(u)
    for v in G[u-1][::-1]:
      Q.append(v)
    

if __name__ == "__main__":
  dfs(con, 1)