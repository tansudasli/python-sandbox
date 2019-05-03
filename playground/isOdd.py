# usage echo 2234 | python3 isOdd.py

input = int(input())


def isOdd(number):
    """determine is number odd or even.  """

    if number % 2 == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(isOdd(input))
