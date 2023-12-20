# from itertools import groupby, cycle, islice, count, chain, dropwhile, takewhile
# from time import perf_counter
# from functools import reduce
#
# #map
# #filter
# #zip
# #reduse
#
#
# # a  = lambda x: x>6
# # print(a(4))
#
# list_number = [a for a in range(1_000_000)]
#
#
# #map
#
# # start = perf_counter()
#
# # def kvadrat(x):
# #     return [i**2 for i in x]
# #
# # print(kvadrat(list_number))
# #
# # end = perf_counter()
# # print(end-start)
#
# # start = perf_counter()
# # print(list(map(lambda x: x**2, list_number)))
# #
# # end = perf_counter()
# # print(end-start)
#
#
# # #filter
# # start = perf_counter()
# #
# # def juft(x):
# #     return [i for i in x if i % 2 == 0]
# #
# # print(juft(list_number))
# # end = perf_counter()
# # print(end-start)
# # print(list(filter(lambda x: x % 2 ==0, list_number)))
#
#
#
# #reduse
# # a = [3, 4,  7]
# # print(reduce(lambda x, y: x*y, a))
#
#
# #zip
#
# # b = ['a', 'b', 'c', 'c']
# #
# # print(list(zip(b, a, list_number)))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# #groupby
#
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # grouped = groupby(numbers, key=lambda x: x < 5)
# # # print(list(grouped))
# #
# #
# # for i, j in grouped:
# #     print(i, list(j))
#
#
# #cycle
#
# colors = ['red', 'green', 'blue', 'yellow']
# cycles = cycle(colors)
# # print(next((cycles)))
# # print(next((cycles)))
# # print(next((cycles)))
# # print(next((cycles)))
# # print(next((cycles)))
# # for _ in range(10):
# #     print(next(cycles))
#
# # limited = islice(cycles, 1, 3)
# # print(next((limited)))
# # print(next((limited)))
#
#
#
#
# #count
#
# # count1 = count(100, -10)
# # print(next(count1))  # 100
# # print(next(count1))  # 110
# # print(next(count1))  # 120
#
#
# #chain
#
# # x = chain("ABCD", "1234")
# # print(list(x))
#
# # y = chain.from_iterable([("ABCD", "1234"), {"ABCD", "1234"}])
# # print(list(y))
#
#
# #dropwhile
#
from itertools import dropwhile, takewhile


# vals = [10, 20, 30, 40,10, 50, 41, 39]
# print(list(dropwhile(lambda x: x<40, vals)))  # [40, 50, 40, 30]
# print(list(takewhile(lambda x: x<40, vals)))  # [10, 20, 30]
# #
#
#
# # cities = {'San Francisco', 'New York', 'Washington DC'}
# # print("New York" in cities)


a = [1, 2, 3]
b = [1, 2]


# s1 = 'salom'
# s2 = 'assalomwdwqsalom'
#
#
# a = s2.replace(s1, '', 1)
# print(a)


# a = 'Assalom Pythonpip'
# a = a.split()
# str_ = ''
# for i in a:
#     b = i[0]
#     d = i.replace(i[0].lower(), '.').replace('.', b, 0)
#     str_ = f"{str_} " + "".join(d)
# print(str_.strip())







