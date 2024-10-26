# def square(n):
#     "Takes in a number n, return the square of a number n"
#     print(n**2)
# square(5)
# print(square.__doc__)

def complex(real, imag):
    """ Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)"""
    if imag == 0.0 and  real == 0.0:
        return complex

complex(0, 0)
print(complex.__doc__)