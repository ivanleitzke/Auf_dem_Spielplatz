def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("start")
print(multiply(1, 2, 3))
print("finish")
# bi.ly/pygist
# f9 add or remove breakpoint
# f10 step over
# f11 step into


# message = "a"


# def greet():
#     #global message
#     message = "b"


# greet()
# print(message)

# def greet():
#     if True:
#         message = "a"
#     print(message)


# def save_user(**user):
#     # print(user)
#     print(user["id"])


# save_user(id=1, name="admin")


# def multiply(*list):
#     total = 1
#     for number in list:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# def increment(number, by):
#     # pass
#     # return number + by

#     return (number, number + by)


# print(increment(2, 3))

# def increment(number, by):
#     # pass
#     # return number + by

#     return (number, number + by)


# print(increment(2, by=4))


# def increment(number, by=3):
#     # pass
#     # return number + by

#     return (number, number + by)


# print(increment(2))

# def increment(number: int, by: int = 3) -> tuple:
#     # pass
#     # return number + by

#     return (number, number + by)


# print(increment(2))
