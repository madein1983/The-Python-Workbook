ELECTRIC_HAMMER = 130
GAS_LAWN_MOWER  = 106   
ALARM = 70
QUIET_ROOM = 40

level_in = int(input("Enter the level of loudness: "))
if level_in < QUIET_ROOM :
    print("The noice level is equial too low less than 40dB")
elif level_in == QUIET_ROOM :
    print("the noise level is equial to quiet room.") 
elif QUIET_ROOM < level_in < ALARM :
    print("The noise level is equial between quiet room and morning alarm.")
elif level_in == ALARM :
    print("The noise level is equial to morning alarm.")
elif ALARM < level_in < GAS_LAWN_MOWER :
    print("The noise level is between morning alarm and gas lawn mower.")
elif level_in == GAS_LAWN_MOWER :
    print("The noise level is equial to gas lawn mower.")
elif GAS_LAWN_MOWER < level_in < ELECTRIC_HAMMER :
    print("The noise level is between gas lawn mower and electric hammer.")
elif level_in == ELECTRIC_HAMMER :
    print("The noise level is equial to electric hammer.")
elif level_in > ELECTRIC_HAMMER :
    print("The noise level is too high for ears. Go go away.")

