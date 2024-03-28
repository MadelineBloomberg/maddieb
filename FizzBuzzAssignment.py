for number in range(1,101):
    if((number % 3) == 0) and ((number % 5) == 0): #if number is a multiple of 3 and 5 print fizzbuzz
        print("fizzbuzz")
    elif((number % 3) == 0): #if number is a multiple of 3, print fizz
        print("fizz")
    elif((number % 5) == 0): #if number is a multiple of 5, print buzz
        print("buzz")
    else:  #else number is not a multiple of 3 print the number
        print(number)
