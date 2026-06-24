letter = input("Enter a letter: ")

if letter == 'a':
  print("The letter is a vowel")

elif letter == 'e':
  print("The letter is a vowel")

elif letter == 'i':
  print("The letter is a vowel")

elif letter == 'o':
  print("The letter is a vowel")

elif letter == 'u':
  print("The letter is a vowel")

else:
  print("The letter is consonant")

import locale

# Set the locale to Indian English to enable Indian numbering format
locale.setlocale(locale.LC_ALL, 'en_IN')

def is_between_one_and_one_crore(number):
    """
    Checks if a number is between 1 and 1,00,00,000 (inclusive).
    1 crore = 1,00,00,000
    """
    return 1 <= number <= 10000000

test_numbers = [1, 2222, 989797, 6656, 55, 56, 54, 566, 777, 888, 776, 7877878, 2342335, 677, 585879]

print("Running Tests:")
print("-" * 45)
for num in test_numbers:
    result = is_between_one_and_one_crore(num)
    status = "Inside" if result else "Outside"
    
    # Use locale.format_string to get the Indian comma placement
    formatted_num = locale.format_string("%d", num, grouping=True)
    
    print(f"Number: {formatted_num:>12} -> {status}")

numbers = [12, -7, 0, -3.5, 45]

for num in numbers:
    if num > 0:
        print(f"{num} is Positive")
    elif num < 0:
        print(f"{num} is Negative")
    else:
        print(f"{num} is Zero")

numbers = [10]

# Filter out zero if you only want strictly positive/negative
positives = list(filter(lambda x: x > 0, numbers))
negatives = list(filter(lambda x: x < 0, numbers))

print("Positives:", positives)
print("Negatives:", negatives)