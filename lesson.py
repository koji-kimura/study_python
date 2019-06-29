l = [1, 2, 3]
del l

i = 5

try:
    l[i]
except IndexError as exc:
    print("IndexError: Don't worry: {}".format(exc))
except NameError as exc:
    print("NameError: Don't worry: {}".format(exc))
except Exception as exc:
    print("other:{}".fotmat(exc))
else:
    print('done')
finally:
    print("clean up")
