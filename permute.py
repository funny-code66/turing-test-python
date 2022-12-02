
def permute(arr, ch) -> set:
  res = set()
  for i in range(len(arr)+1):
    res.add(arr[:i]+ch+arr[i:])
    res.add(arr[i:]+ch+arr[:i])
  return res

def permutations(arr) -> set:
  res = set()
  for i, ch in enumerate(arr):
    res.update(permute(arr[:i]+arr[(i+1):], ch))
    res.update(permute(arr[(i+1):]+arr[:i], ch))
  return res

if __name__ == "__main__":
  # arr = [v for v in input().strip().split(',')]
  print(permutations("aabc"))