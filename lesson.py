from collections import defaultdict
s = "fhlsdkfhksdhgksdh;lsdhh;fdgh;fdhg"

d = {}

# for c in s:
#     if c not in d:
#         d[c] = 0
#     d[c] += 1

# print(d)

# for c in s:
#     # 辞書にはデフォルト値を設定できる
#     d.setdefault(c, 0)
#     d[c] += 1

# 上記のようにしなくても組み込み関数でできる
d = defaultdict(int)
for c in s:
    d[c] += 1

print(d)

print(d['f'])
