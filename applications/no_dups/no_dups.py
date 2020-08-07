def no_dups(s):
    # Removed duplicated words in string
    # split the string into a list of words
    lst = s.split(' ')
    # create a indexed list for storing words without duplication, 
    # this way time complexity reduces to O(n)
    new = {}
    # count the word added in the indexed list
    count = 0
    for word in lst:
        if word not in new:
            count += 1
            new[word] = count

    # join the index for the indexed list as output
    results = " ".join(list(new.keys()))      
    return results  
    
if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))