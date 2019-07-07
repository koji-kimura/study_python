# f = open('test.txt', 'w')
with open('test.txt', 'w') as f:
    print('\n print', file=f)
