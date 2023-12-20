from decorator_adv import timer

# def decorator_func(orinal_func):
#     def wrapper_func(*args, **kwargs):
#         print(f"Original funv {orinal_func.__name__}")
#         values = orinal_func(*args, **kwargs)
#         values = (f"{values} developer")
#         print(values)
#         return values
#     return wrapper_func



# @decorator_func
# def get_name(name):
#     return name
#
# get_name('Bahodir')


# func_ = decorator_func(get_name)
# print(func_("Shaxriyor"))


# def yigibdi(x):
#     def c_func(y):
#         return x+y
#     return c_func
#
# f = (yigibdi(12))
# print(f(2))
#
#
# def hello_func(name):
#     def hello(age):
#         return f"Hello {name}, {age}"
#     return hello
#
# a = hello_func("Shaxriyor")
# print(a(23))


# def son1(x):
#     def daraja(y):
#         return x**y
#     return daraja
#
#
# s = son1(4)
# print(s(2))


# def decorator_func(original_func):
#     def wrapper(*args, **kwargs):
#         v = original_func(*args, **kwargs)
#         d = [i**2 for i in v if i > 0]
#         return d
#     return wrapper
#
#
# @decorator_func
# def sonlar(son):
#     return son
#
# print(sonlar([2, 6, -4, 7, -2]))




@timer
def kvadrat(sonlar):
    return [i**2 for i in sonlar]

list_num = range(10)

kvadrat(list_num)





