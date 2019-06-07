import time


def time_c(func):
    def wrapper(*args, **kwargs):
        #start = time.perf_counter()
        start = time.time()
        func(*args, **kwargs)
        #elapsed = (time.perf_counter() - start)
        elapsed = (time.time() - start)
        print("{} : Time used: {}".format(func.__name__, elapsed))
    return wrapper


def binary_search(lst, data):
    n = len(lst)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if lst[mid] > data:
            last = mid - 1
        elif lst[mid] < data:
            first = mid + 1
        else:
            return mid, True
    return False


def normal_search(lst, data):
    for i, num in enumerate(lst):
        if num == data:
            return i, True
    return False


binary_list = [i for i in range(10000)]
data = 3167


@time_c
def binary_test():
    print(binary_search(binary_list, data))


@time_c
def index_test():
    try:
        print((binary_list.index(data), data in binary_list))
    except BaseException:
        print(False)


@time_c
def normal_test():
    print(normal_search(binary_list, data))


binary_test()
index_test()
normal_test()
