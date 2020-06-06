import time

def count_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end-start))
        return result
    return wrapper


# @count_time
# def time_test():
#     time.sleep(5)

# time_test()