function update(set, ele) {
  if (!set.includes(ele)) set.push(ele)
  return set
}

function updateArray(set, set2) {
  set2.map((ele)=>{
    if (!set.includes(ele)) set.push(ele)
  })
  return set
}

function insert(arr, ch) {
  res = []
  for (let i = 0; i<arr.length+1; i++) {
    res = update(res, arr.slice(0, i) + ch + arr.slice(i))
    // console.log(res)
    res = update(res, arr.slice(i) + ch + arr.slice(0,i))
    // console.log(res)
  }
  return res
}

function permutations(arr) {
  res = []
  for (let i = 0; i<arr.length; i++) {
    res = updateArray(res, insert(arr.slice(0, i)+arr.slice(i+1), arr[i]))
    res = updateArray(res, insert(arr.slice(i+1)+arr.slice(0, i), arr[i]))
  }
  return res;
}

console.log(permutations("aabc"))