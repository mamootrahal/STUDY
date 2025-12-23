s = list(map(str, input()))

pairs = {')': '(', ']': '[', '}': '{', '>': '<'}

st = []
ok = True

for i in range(len(s)):
    ch = s[i]

    if ch in pairs.values():          # открывающая
        st.append(ch)
    elif ch in pairs.keys():          # закрывающая
        if len(st) == 0 or st[-1] != pairs[ch]:
            ok = False
            break
        st.pop()
    else:
        continue

if ok and len(st) == 0:
    print("YES")
else:
    print("NO")
