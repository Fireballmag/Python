from random import randint

def change(a, b):
    bufer = a
    a = b
    b = bufer
    return a, b

c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)
f = randint(0, 10)
print(f"c = {c}, d = {d}, e = {e}, f = {f}")

c, d = change(c, d)
print(f"After the changes c and d {c, d}")

e, f = change(e, f)
print(f"After the changes e and f {e, f}")

d, e = change(c, d)
print(f"After the changes d and e {d, e}")


