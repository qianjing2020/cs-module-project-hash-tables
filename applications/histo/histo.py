# Your code here
# special character to be ignored
special = ' " : ; , . - + = / \ | [ ] { } ( ) * ^ & '

def word_hist(filename):
    # get text from the txt file
    f = open(filename, "r")
    text = f.read()
    f.close()
    
    # remove all line breaks
    text = text.replace('\n', ' ')

    # create a text list
    words = text.split(" ")
    #words.remove("\n")
    # creat an indexed list for word count
    word_counts = {}
    
    # loop through the words list
    for word in words:       
        if word not in word_counts:
            word_counts[word] = 0
        # otherwise, add 1 to count and store it
        
        word_counts[word] += 1
    
    lst = sorted(word_counts.items(), key = lambda x: (x[1], x[0]), reverse=True)
    
    for a in lst:
        print(f"{a[0]:{10}} {a[1]*'#':{20}}" )

    return word_counts

if __name__ == "__main__":
    filename = 'applications/histo/robin.txt'
    word_hist(filename)    