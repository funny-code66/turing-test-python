
result = 0
stack, direction, visited = [root], {root: 1}, set()
while stack:
  v = stack.pop()
  if v in visited:
    continue
  visited.add(v)

  if v.left is None and v.right is None and direction[v]=='left':
    result += v.val

  if v.left is not None:
    stack.append(v.left)
    direction[v.left]= 'left'

  if v.right is not None:
    stack.append(v.right)
    direction[v.right]= 'right'
    
return result