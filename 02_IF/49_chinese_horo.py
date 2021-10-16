CYCLE = 12
DRAGON = 2000
SNAKE = 2001
HORSE = 2002
GOAT = 2003
MONKEY = 2004
ROOSTER = 2005
DOG = 2006
PIG = 2007
RAT = 2008
BULL = 2009
TIGER = 2010
RABBIT = 2011
a = (2026-2000) % 12
print (a)

year_in = int(input("Enter the year like 2000: "))
a = (year_in - 2000) % 12
if a == 0 :
    chineese_year_is = "Dragon"
elif a == 1 :
    chineese_year_is = "Snake"
elif a == 2 :
    chineese_year_is = "Horse"
elif a == 3 :
    chineese_year_is = "Goat/Sheep"
elif a == 4 :
    chineese_year_is = "Monkey"
elif a == 5 :
    chineese_year_is = "Rooster"
elif a == 6 :
    chineese_year_is = "Dog"
elif a == 7 :
    chineese_year_is = "Pig"
elif a == 8 :
    chineese_year_is = "Rat"
elif a == 9 :
    chineese_year_is = "Bull"
elif a == 10 :
    chineese_year_is = "Tiger"
elif a == 10 :
    chineese_year_is = "Rabbit"


print(chineese_year_is)