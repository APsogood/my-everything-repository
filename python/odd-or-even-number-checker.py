def is_odd_or_even(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

test_numbers = [4, 7, 13, 28, 45, 90]

for number in test_numbers:
    result = is_odd_or_even(number)
    print(f'{number} is {result}.')
