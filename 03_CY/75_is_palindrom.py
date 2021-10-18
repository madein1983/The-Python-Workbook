line_in = input("Enter the text: ")
is_palindrom = True
i = 0
while i <= len(line_in)/2 and is_palindrom:
        if line_in[i] != line_in[len(line_in)-i-1] :
            is_palindrom = False
        i = i + 1
if is_palindrom :
    print("The phrase is palindrome.")
else:
    print("The phrase is NOT palindrome.")

    
    


            
            
