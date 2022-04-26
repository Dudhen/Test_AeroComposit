def written_func(a):
    def written_func_2(*args):
        if args:
            return written_func(a + args[0])
        else:
            return a
    return written_func_2


print(written_func(15)(30)(-10)())