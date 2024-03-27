from random import randint

def IsPositiveNumber(a):
    if(a > 0):
        return True
    elif(a == 0):
        return "0 - idiot"
    else:
        return False

N1 = randint(-10, 10)
N2 = randint(-10, 10)
N3 = randint(-10, 10)
N4 = randint(-10, 10)
N5 = randint(-10, 10)
print(N1, IsPositiveNumber(N1), N2, IsPositiveNumber(N2), N3, IsPositiveNumber(N3), N4, IsPositiveNumber(N4), N5, IsPositiveNumber(N5))
