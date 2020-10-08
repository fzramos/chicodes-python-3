def palindrome(word):
    # if word == word[::-1]:
    #     return True
    # return False

    # this works but is a very inefficient way to do this since you're already
    # given a conditional True False statement 
    # If you wanted to return a string or print something, then the if-else
    # would have purpose

    return word == word[::-1]


while True:
    user_word = input("Type a word and I'll let you know if its a palindrome:\nYour word: ")
    if palindrome(user_word):
        print(f'Yes, the word {user_word} is a palindrome!')
    else:
        print(f'No, the word {user_word} is not a palindrome.')
    cont = input('Would you like to continue? ')
    if cont == 'n':
        print("Have a great day!")
        break

