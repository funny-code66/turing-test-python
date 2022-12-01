
result = 1
stack, depth,, visited = [root], {root: 1}, set()
while stack:
  v = stack.pop()
  if v in visited:
    continue
  visited.add(v)

  if result < depth[v]:
    result = depth[v]

  if v.left is not None:
    stack.append(v.left)
    depth[v.left]= depth[v]+1

  if v.right is not None:
    stack.append(v.right)
    depth[v.right]= depth[v]+1
