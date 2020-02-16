import sys


def plus10(num):
    return num + 10


# name = "Elad"
# age = 45
#
# print(f"The name is {name.lower()} and the age is {age + 10}")


arr = [1, 3, 55, 10]

arr2 = [n + 10 for n in arr]

arr3 = list(map(plus10, arr))
# arr4 = filter(lambda n: n % 2 == 0, map(lambda num: num + 15, arr))

# for i in range(len(arr)):
#     print(arr[i])

# print(arr3)

# for n in arr:
#     print(n, arr3[arr.index(n)])

# for m in arr:
#     print(f"{m} , {n}")
# print(arr2)

# for i in range(len(arr)):
#     print(arr[i], arr3[i])

# arr5 = [(1, 2), (3, 6)]
#
# print(zip(arr, arr3))
#
# for num1, num2 in zip(arr, arr3):
#     print(num1, num2, num2 - num1)

# a, b = arr5[1]
# print(a, b)


# def print_me(name="bob", age=10):
#     print(f"The name is {name.lower()} and the age is {age + 10}")
#
# name = "Mor"
# print_me(name)

class Foo:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b


f = Foo(3, 16)
d = vars(f)
# print(d["a"])

print(sys.argv[1])


def foo(s, change_func=None):
    res = ".".join(s.split(","))
    if change_func:
        res = change_func(res)

    return res


