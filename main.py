# it works slow af
# and idk why
# but tbh i dont care
# made by me
import sys

result = 0


# it still warns tf
def addition(result=result, *args):
    for i in args[0:]:
        result += i
    return result


def subtraction(result=result, *args):
    for i in args[0:]:
        result -= i
    return result


def multiplication(result=result, *args):
    for i in args[0:]:
        result *= i
    return result


def division(result=result, *args):
    for i in args[0:]:
        result /= i
    return result


if __name__ == '__main__':
    for i in range(len(sys.argv[1:])):
        sys.argv[1+i] = int(sys.argv[1+i])
    result = sys.argv[2]
    if sys.argv[1] == 1:
        print(addition(*sys.argv[2:]))
    if sys.argv[1] == 2:
        print(subtraction(*sys.argv[2:]))
    if sys.argv[1] == 3:
        print(multiplication(*sys.argv[2:]))
    if sys.argv[1] == 4:
        print(division(*sys.argv[2:]))

