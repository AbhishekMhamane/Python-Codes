import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ +"has taken " + str((end - start)*1000) + "mili sec")
        return result
    return wrapper

@time_it
def processList(list):
    re = []
    for i in list:
        re.append(i)
    

array = range(1,1000000)
processList(array)