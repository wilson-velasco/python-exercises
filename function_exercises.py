# 1. Define a function named is_two. It should accept one input and return True if the passed input is 
# either the number or the string 2, False otherwise.

def is_two(x):
    return x == 2 or x == '2'
    
# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(x):

    return x.lower() in list('aeiou')
    
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(x):
    
    return not is_vowel(x)
    
# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter 
# of the word if the word starts with a consonant.

def first_letter_capped(word):
    if is_consonant(word[0]):
        return word.capitalize()
    else:
        return word

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total, and return the amount to tip.

def calculate_tip(bill_percent, bill_total):
    return "Amount to tip: " + str(bill_percent * bill_total)

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    final_price = original_price - (original_price * discount_percent)
    return final_price

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it 
# as input, and return a number as output.

def handle_commas(number):
    return int(number.replace(',',''))

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(num_grade):
    if 88 <= num_grade <= 100:
        return 'A'
    elif 80 <= num_grade <= 87:
        return 'B'
    elif 67 <= num_grade <= 79:
        return 'C'
    elif 60 <= num_grade <= 66:
        return 'D'
    elif num_grade <= 59:
        return 'F'

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowel(x):
    for char in x:
        if is_vowel(char):
            x = x.replace(char,'')
    return x

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#  - anything that is not a valid python identifier should be removed
#  - leading and trailing whitespace should be removed
#  - everything should be lowercase
#  - spaces should be replaced with underscores
#    for example:
#      - Name will become name
#      - First Name will become first_name
#      - % Completed will become completed

def normalize_name(name):
    import re
    name = re.sub('[!@#$%^&*.]','', name)
    name = name.strip().lower().replace(' ','_').strip('_')
    return name

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the 
# cumulative sum of the numbers in the list.

#     - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#     - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list_of_nums):
    new_list = []
    
    for num in list_of_nums:
        new_list.append(sum(list_of_nums[:num]))
                        
    return new_list