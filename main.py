user_input = int(input("Enter an integer: "))

def multiply_digits(number):
    while number > 9:
        digits = [int(digit) for digit in str(number)]
        product = 1
        for digit in digits:
            product *= digit
        number = product
    return number

result = multiply_digits(user_input)
print(result)
