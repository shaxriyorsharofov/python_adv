import timeit

# a: int = 4
# b: int  = a
# b: int = 2
# del a
# print(b)

#


# def sume1(a, b):
#     return b + a
# # sume1(2,5)
# v = timeit.timeit(sume1(3, 6), number=1)
# print(v)






# start_code = time.time()
#
# def sume(a: int, b:int) ->int:
#     return b
# sume(2,5)
#
# end_code = time.time()
# result = end_code - start_code
#
# print(result)



#
# import timeit
#
# # Tekshirishni kerak bo'lgan funksiya
# def my_function():
#     result = sum(range(1000))
#
# # timeit modulini ishlatib, funksiyani bajarish vaqtini o'lchamiz
# execution_time = timeit.timeit(my_function, number=1000)
#
# # Natijani chiqaramiz
# print(f"My function took {execution_time} seconds to execute 10,000 times.")




# my_script.py

from memory_profiler import profile
#
# @profile
# def my_function():
#     a = [1] * (10 ** 6)  # Misol uchun katta ro'yxat yaratamiz
#     b = [2] * (2 * 10 ** 7)  # Yana bir katta ro'yxat yaratamiz
#     b = 'webfuyqefybqeryu'
#     b = [i for i in range(10000)]
#     # b = 1  # b o'zgaruvchisini yo'q qilamiz
#     return a, b
#
# if __name__ == '__main__':
#     my_function()
#
#
# print([1]*5)




a = [1, 2, 3]
b = [1, 2, 3]

print(a==b)
print(a is b)