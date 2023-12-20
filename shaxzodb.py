# # a = int(input("Son kiriting:"))
# # s = 0
# #
# # if a >= 0:
# #     if a == 0:
# #         print(-1)
# #     else:
# #         b = [i for i in range(-1 * a, a+1)]
# #         for i in range(len(b)):
# #             for j in range(i, len(b)):
# #                 if b[i] * b[j] == a:
# #                     s += 1
# #         print(s)
# # else:
# #     b = [i for i in range(a, (a*-1)+1)]
# #
# #     for i in range(len(b)):
# #         for j in range(i, len(b)):
# #             if b[i] * b[j] == a:
# #                 s += 1
# #     print(s)
#
#
# n,k = map(int,input().split())
# s = 2
# x = 0
# sum_ = 0
# if n==0:
#   print(1)
# d = []
# while n:
#     for i in range(1,s):
#         sum_ += k+1
#         s = sum_
#     n -=1
#     d.append(sum_)
# print(d[-1])
from collections import namedtuple
from decimal import Decimal
from math import floor

# a = Decimal("0.11")
# b = Decimal("0.1")
# c = Decimal("0.1")
# d = Decimal("0.31")
# print(d == (a+b+c))
# print(format(a, '.300f'))
# print(round(d,3) == round((a+b+c), 3) )

# print(round(a, 1))

P = namedtuple('Person', '_age, _name', rename=True)

person1 = P('21', 'Shaxriyor')
person2 = P('20', 'Shaxzor')
# print(person1.age)
# x, y = person2
# print(x, y)

# for i in person1:
#     print(i)

# print(isinstance(person2, P))
# print((isinstance(person2, tuple)))

print(P._fields)