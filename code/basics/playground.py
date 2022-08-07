def sayDamnYou(name):
    return 'Damn you' + ', ' + name

print(sayDamnYou('Ezikel'))

def executeTheFunc(func, param):
    return func(param);

result = executeTheFunc(sayDamnYou, "Bro!")
print(result)

# Currying
summation = 0;
def curry(digit, ender=False):
    global summation
    summation += digit
    if ender:
        return summation
    return curry

curryResult = curry(10)(9)(8)(7)(6)(5, True) # Expected: 45
print(curryResult)