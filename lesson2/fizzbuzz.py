sameline = ""
fizz = "fizz"
buzz = "buzz"
fizzbuzz = "fizzbuzz"
def simplest_arithmetic_sequence(n):
    for i in range(1, n+1):
        if i % 3 == 0:
            sameline = fizz
            if i % 5 == 0:
                sameline = fizzbuzz
            print(sameline)
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

simplest_arithmetic_sequence(20)