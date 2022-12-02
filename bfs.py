con = [
  {2, 3, 4},
  {5, 6},
  {},
  {7, 8},
  {9, 10},
  {},
  {11, 12},
  {},
  {},
  {},
  {},
  {},
]

def bfs(G, s):
  """ G: graph, s: root node, q: queue, P={s:None}: parent """
  P={s:None}
  Q=[]; Q.append(s), print(s)
  while Q:
    u = Q.pop(0)
    for v in G[u-1]:
      if v in P: continue
      P[v] = u
      Q.append(v)
      print(v)
  print(P)

if __name__ == "__main__":
  bfs(con, 1)