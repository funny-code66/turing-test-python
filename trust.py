for i in range(N):
  man = i+1
  res = -1
  flag = "Judge"
  num=0
  for trust_ele in trust:
    if man==trust_ele[0]:
      flag="NotJudge"
      break
    if man==trust_ele[1]:
      num += 1
  if flag == "Judge" and num == N:
    res = man
    break
return res