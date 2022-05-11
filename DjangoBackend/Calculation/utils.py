def myCheckInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def myCheckPositive(str):
    if(int(str) < 0):
        return False
    else:
        return True
