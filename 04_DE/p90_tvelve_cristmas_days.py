import p89_number_to_numeral

def main():
    for i in range(1,13) :
        print("On the ",p89_number_to_numeral.numeral(i), "day of Crismas")
        print(" my true love sent me ")
        if i == 12 : 
            print("Twelve Drummers Drumming")  
        if i >= 11 :
            print("Eleven Pipers Piping")
        if i >= 10 :
            print("Ten Lords a Leaping")
        if i >= 9 :
            print("Nine Ladies Dancing")
        if i >= 8 :
            print("Eight Maids a Milking")
        if i >= 7 :
            print("Seven Swans a Swimming")
        if i >= 6 :
            print("Six Geese a Laying")
        if i >= 5 :
            print("Five Golden Rings")
        if i >= 4 :
            print("Four Calling Birds")
        if i >= 3 :
            print("Three French Hens")
        if i >= 2 :
            print("Two Turtle Doves")            
        
        
        
        
        
        
        
        
        
                             
        
        print("A partrige in a pear tree")
        print("*_________________________* ")


if __name__ == "__main__":
    main()