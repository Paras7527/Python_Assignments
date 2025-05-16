def CheckPrime(iNo):
    if iNo <= 1:
        return False
    for i in range(2, iNo):
        if iNo % i == 0:
            return False
    return True