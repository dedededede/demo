a = [3, 1, 2, 4]
def sort1(s, l, r):
  i = l
  j = r
  x = s[l]
  while i < j:
    while i < j and s[j] >= x:
        j -= 1

    if i < j:
      s[i] = s[j]
      i += 1

    while i < j and s[i] < x:
       i += 1

    if i < j:
      s[j] = s[i]
      j -= 1

    s[i] = x
    return i

def sort(s, l, r):
  if l < r:
    middle = sort1(s, l, r)
    sort(s, l, middle - 1)
    sort(s, middle + 1, r)

sort(a, 0, len(a) - 1)
print a