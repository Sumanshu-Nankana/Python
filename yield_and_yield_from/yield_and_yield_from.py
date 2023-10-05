def return_statement(n):
    squares = []
    for i in range(n):
        squares.append(i**2)
    return squares


print(return_statement(5))
#
# ####################################
#


def yield_statement(n):
    for i in range(n):
        yield i**2


for i in yield_statement(5):
    print(i)

#############################################


def generator1():
    yield 100
    yield 101
    yield 102


def generator2():
    yield from generator1()
    yield 201
    yield 202
    yield 203


for i in generator2():
    print(i)

#########################################


def generator3():
    for i in range(1, 11):
        yield i


def generator4():
    for i in range(11, 21):
        yield i


def generator5():
    yield from generator3()
    yield from generator4()


for i in generator5():
    print(i)
