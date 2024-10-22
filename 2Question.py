##Question2:
##Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
##Suppose the following input is supplied to the program:
##without,hello,bag,world
##Then, the output should be:
##bag,hello,without,world
##
##Hints:
##In case of input data being supplied to the question, it should be assumed to be a console input.

INPUT = input("Enter the words by using comma") #Console Input
words=INPUT.split(",")                          #Split the words and atore in list
words.sort()                                    #sort the list
output= ",".join(words)                         #Join the string with Comma
print(type(output))                   
print("The sorted order of the given input is -",output)
