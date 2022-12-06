visited = set()
def subset(arr, n)-> list[str]:
  if n == 1:
    return [arr]
  
  res = []
  for ele in arr[::-1]:
    subarr = [subele for subele in arr if subele != ele]
    if str(subarr) in visited:
      continue
    visited.add(str(subarr))
    res = res + subset(subarr, n-1)
    # print(subarr)
  res = res + [arr]
  return res

print(subset([1, 2, 3, 4], 4))
