
def list_of_denumerators(line_in):
    i = 2
    self_denumerators_arr = []
    while i <= line_in :
        if (line_in % i) == 0 :
            self_denumerators_arr.append(line_in//i)
            i +=1    
        else : 
            i +=1
    return self_denumerators_arr

def main():
    
    line_in = int(input("Enter number: "))
    print(list_of_denumerators(line_in))
    print("end of executing imported module p115_list_of_personal_denomunators.py")

