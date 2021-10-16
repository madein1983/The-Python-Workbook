GEORGE_WASHINGTON = 1
THOMAS_JEFFERSON = 2
ABRAHAM_LINKOLN = 5
ALEXANDER_HAMILTON = 10
ENDRY_JACKSON = 20
ULISS_GRANT = 50
BENJAMIN_FRANKLIN = 100

cash = int(input("Enter the value of cash bill: "))
if   cash == GEORGE_WASHINGTON :
    portrait = "George Washington"
elif cash == THOMAS_JEFFERSON :
    portrait = "Thomas Jefferson"
elif cash == ABRAHAM_LINKOLN :
    portrait = "Abraham Linkoln"
elif cash == ALEXANDER_HAMILTON :
    portrait = "Alexander Hamiltom"
elif cash == ENDRY_JACKSON :
    portrait = "Endry Jackson"
elif cash == ULISS_GRANT :
    portrait = "Uliss Grant"
elif cash == BENJAMIN_FRANKLIN :
    portrait = "Benjamin Franklin"
else :
    portrait = "There is no such bill"
print("Teh name of person is: ",  portrait)