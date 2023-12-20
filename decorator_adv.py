

def timer(original_func):

    def wrapper(*args, **kwargs):
        from time import perf_counter
        value = original_func(*args, **kwargs)


        for i in value:
            t1 = perf_counter()

            print(i)

            t2 = perf_counter() - t1
            print(f"{i} : {t2}")



    return wrapper