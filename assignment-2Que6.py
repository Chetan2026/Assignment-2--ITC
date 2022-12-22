print(" Q6 For any three lengths, there is a simple test to see if it is possible to form a triangle. If any of the three lengths is greater than the sum of the other two,then you cannot form a triangle. Otherwise, Enter three sides of a triangle, converts them to integers, and to check whether the given input lengths can form a triangle or not (Print : “Yes” or “No”) ")

      
### input from user  ###
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))
 
if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")