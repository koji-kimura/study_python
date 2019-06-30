# print()、next()も組み込み関数
print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95,
}
# 配列.get(key)で値をとる
print(ranking.get('A'))

# getで取ってきた値をキーにしてソートをかける
print(sorted(ranking, key=ranking.get, reverse=True))
