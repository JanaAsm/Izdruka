for x in range(1,100):
    if x % 5 == 0 and 7 == 0:
        print("FizzBuzz", end=', ')
    elif x % 5 == 0:
        print("Fizz", end=', ')
    elif x % 7 == 0:
        print("Buzz", end=', ')
    else:
        print(x, end=', ')