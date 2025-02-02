def kmp(s, t):
    indices = []
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k-1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            indices.append(i - len(s) + 1)
            k = f[k-1]
    return indices


def prefix(s):
    v = [0]*len(s)
    for i in range(1, len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


pattern = "a"
text = "ababcababcabc"
print(kmp(pattern, text))
