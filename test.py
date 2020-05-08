from math import log
def reshape(number=1):
    if number != 0:
        return int(log(number, 4))

def check_int (number):
    if int(number)==number:
        return int(number)
    else:
        return number
x=0.0
print(check_int(x))
