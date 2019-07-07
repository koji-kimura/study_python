# f = open('test.txt', 'w')
f = open('test.txt', 'a')
# flie = fを入れないと普通にコンソールに吐き出されるだけ
print('\n print', file=f)
f.close()
