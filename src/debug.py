import timeit


def clock(func):
    def clocked(*args, **kwargs):
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        run_time = timeit.default_timer() - start
        func_name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('调用>>>%s 耗时>>>%0.8fs' % (func_name, run_time))
        return res

    return clocked
