#run-command
# echo 2234 | python3 isOdd.py

input = int(input())


def isOdd(number):

    return number % 2 != 0

    # return False if number % 2 == 0 else True

    # if number % 2 == 0:
    #     return False
    # else:
    #     return True


if __name__ == '__main__':
    print(isOdd(input))
