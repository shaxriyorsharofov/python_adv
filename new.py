# CLOSURE

def hello_func(name):
    def hello(age):
        return f"Hello {name}, {age}"
    return hello

a = hello_func("Shaxriyor")
print(a(23))





# DRY

def decorator_func(original_func):

    def wrapper_func(*args, **kwargs):
        print('Original funksiya nomi {}'.format(original_func.name))
        new_value = original_func(*args, **kwargs)
        new_value = f"{new_value} aka"
        print(new_value)
        return new_value

    return wrapper_func


@decorator_func
def func_(name):
    return f"Hello {name}"

func_('Shaxzod')

deco = decorator_func(func_)
deco('Shaxriyor')





def decorator_num(original_func):
    def wrapper_func(*args, **kwargs):
        print('{}'.format(original_func.name))
        values = (original_func(*args, **kwargs))
        values = [i for i in values if i % 2 == 0]
        print(values)
        return values
    return wrapper_func


def numbers_(nums):
    return nums


deco = decorator_num(numbers_)
deco([5, 8, 9])



def my_timer(original_func):
    def wrapper_func(*args, **kwargs):
        from time import perf_counter
        t1 = perf_counter()
        result = original_func(*args, **kwargs)
        t2 = perf_counter() - t1
        print(f"{original_func.name} run: {t2} second")
        return result
    return wrapper_func


@my_timer
def info_func(name, age):
    return f"Name: {name}\nAge: {age}"
print(info_func("Shaxriyor", '21'))


def divide_decorator(func):
    def divide_inner(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print("Nolga bo'lish mumkin emas!")

    return divide_inner


@divide_decorator
def divider(a, b):
    return a / b


print(divider(10, 5))  # 2.0
print(divider(10, 0))  # Nolga bo'lish mumkin emas!







from contextlib import contextmanager


class FaylMenejeri:
    def init(self, file_name, mode_):
        self.file_name = file_name
        self.mode_ = mode_

    def enter(self):
        self.fayl = open(self.file_name, self.mode_)
        return self.fayl

    def exit(self, t, d, f):
        self.fayl.close()

# Context manager ni ishlatish
file_name = "test.txt"
mode_ = "w"

with FaylMenejeri(file_name, mode_) as fayl:
    fayl.write("Bu faylga yozilgan matn.")



@contextmanager
def fayl_menejeri(fayl_nomi, usuli):
    fayl = open(fayl_nomi, usuli)
    yield fayl
    fayl.close()

# Context manager ni ishlatish
fayl_nomi = "test.txt"
usuli = "w"

with fayl_menejeri(fayl_nomi, usuli) as fayl:
    fayl.write("Bu faylga yozilgarrrrn matn.")
# "with" blok tugaganda, fayl avtomatik ravishda yopiladi