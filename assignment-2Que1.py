print("ASSIGNMENT 2")

print(" Q1 For a given input string “Python is a case sensitive language”. Write python code for the following")

###input from the user ###
      
input_str = "Python is a case sensitive language"
print("(a)\tThe length of the given string is : %s" % len(input_str))

###reverse string creation ###      
reversed_str = input_str[ : : -1 ]                                                                         
print("(b)\tThe string in reverse would be : %s" % reversed_str)

###creation of new string ###      
new_str = input_str[10:26]                                                                                               
print("(c)\tThe new string becomes : %s" % new_str)

###replacing value and formation of duplicate input ###      
dup_input_str = input_str.replace("a case sensitive", "object oriented")                                    
print("(d)\tThe replaced substring will be : %s" % dup_input_str)
substr = "a"
indx = input_str.find(substr)                                                                               
if indx == -1:
    print("(e)\tThe given substring was not found in the inputted string")
else:
    print("(e)\tThe first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))

###removal of white spaces ###
no_white_spaces_str=input_str.replace(" ","")                                                               
print("(f)\tThe inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)
