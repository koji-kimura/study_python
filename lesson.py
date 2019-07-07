s = """\
AAA
BBB
CCC
DDD
"""

# with open('test.txt', 'w') as f:
#     f.write(s)

with open('test.txt', 'r+') as f:
    f.write(s)
    # 書き込んでしまったので最後に戻ってしまっている
    f.seek(0)
    print(f.read())
