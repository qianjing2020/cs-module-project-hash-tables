import re

def word_count(s):
    #  init dict for word count
    count = {}
    # string has no alphabet or numbers
    # if re.match('A-Za-z0-9')
    # empty string
    if s == "":
        return count
    # generate unwanted list of special characters
    special = ' " : ; , . - + = / \ | [] {} () * ^ & '
    special_lst = special.split()
    
    # use gen exp to reconstruct the clean version of the text
    text = "".join(item.lower() for item in s if item not in special_lst)

    # remove extra space:
    text = re.sub(' +', ' ', text)
    print(text)
    
    lst = text.split(" ")
    for x in lst:
        if x not in count:
            count[x] = 0
        # if found a repeat, add 1
        count[x] += 1      
            
    return count

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello    hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
