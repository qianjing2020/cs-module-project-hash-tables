# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
special = ' " : ; , . - + = / \ | [] {} () * ^ & '

def alphabet_frequency(filename):
    #obtain text from txt file
    f = open(filename, 'r')
    s = f.read()
    f.close
    # list contains list of alphabets
    lst = s.replace(" ", "")
    # remove all special character
    lst = [c for c in lst if c.isalnum()]
    # creat an dictionary to count frequency
    letter_count = {}
    for letter in lst:
        if letter not in letter_count:
            letter_count[letter] = 0
        letter_count[letter] += 1 

    # sort the dictionary by value frequency
    list_sorted = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
     # match the frequency to get cipher map!
    list_sorted =  list_sorted[:-1]
    print(len(list_sorted))
    frequent_english = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

    cipher_map = zip(tuple(list_sorted.items[0], frequent_english))

    deciphered = lst
     
    return cipher_map

result = alphabet_frequency('applications/crack_caesar/ciphertext.txt')
print(result)
