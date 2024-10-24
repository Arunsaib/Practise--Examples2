##Question4:
##Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
##Suppose the following input is supplied to the program:
##hello world and practice makes perfect and hello world again
##Then, the output should be:
##again and hello makes perfect practice world
##
##Hints:
##In case of input data being supplied to the question, it should be assumed to be a console input.
##We use set container to remove duplicated data automatically and then use sorted() to sort the data.

INPUT = input("Enter a sequence of words: ")
UNIKwords = []
Duplicate=[]
words = INPUT.split()


for I in words:
    
    Isunique = True
    
   
    for J in UNIKwords:
        if I == J:
           Duplicate.append(J)
           Isunique = False
           break  
    
   
    if Isunique==True:
        UNIKwords.append(I)
UNIKwords.sort()
output = ' '.join(UNIKwords)
Duplicateout=' '.join(Duplicate)
print("List without Duplicates and sorted order-",output)
print("List with Duplicates are-",Duplicateout)


