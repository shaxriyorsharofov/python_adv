# my_list = [2, 4, 8, 16, 32]
#
# iterator = iter(my_list)
import np

# for i in range(2):
# print(next(iterator))  # 2
# print(next(iterator))  # 4
# print(next(iterator))  # 8
# print(next(iterator))  # 16
# print(next(iterator))  # 32
# print(next(iterator))  # StopIteration
# print(next(iterator))  # StopIteration
# for i in my_list:
#     print(i)

#
#
#
# List yaratish
# mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Holi"]
#
# # List iteratorini olish
# iterator = iter(mehmonlar)
#
# # List ichidagi elementlarni chiqarish
# while True:
#     try:
#         mehmon = next(iterator)
#         print(mehmon)
#     except StopIteration:
#         break



# def generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# d = generator()
# print(type(next(d)))
# a = next(d)
# b = next(d)
# c = a+b
# print(c)



# for value in generator():
#     print(value)
# # 1
# # 2
# # 3
#
# # my_generator = generator()
# #
# # print(next(my_generator))  # 1
# # print(next(my_generator))  # 2
# # print(next(my_generator))  # 3
# # print(next(my_generator))  # StopIteration
#
#
#
#
#
# #
# def square(nums):
#     for num in nums:
#         yield num ** 2
#
#
# numbers = [1, 2, 3]
# generator = square(numbers)
#
# print(next(generator))  # 1
# print(next(generator))  # 4
# print(next(generator))  # 9
# print(next(generator))  # StopIteration
#
#
# numbers = [1, 2, 3]
# sum_of_square_numbers = sum(square(numbers))
# print(sum_of_square_numbers)  # 14



# for i in range(3, 7, 2):
#     print(i)


# for i in np.arange(0.5, 6.5, 1.5) :
#     print(i)