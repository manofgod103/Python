def mul_9(num):
    if num >= 1:
        mul_9(num - 1)
    else:
        return 1
    for m in range(1, num + 1):
        print("%d*%d=%d" % (m, num, m * num), end="\t")
    print()

mul_9(9)
