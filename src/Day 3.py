#Day 3:- Conditional Statements, Logical Operators, code Block and scope
print(f'Welcome to the Treasure Island\nYou are in a mission to find Treasure')
print(f'You moved towards the crossroad')
crossRoad = input('You reached the crossroad, Would you like to take Right or Left? (L/R)')
if(crossRoad == "L"):
    print('You have choosen Left, Walked for few minutes. Found a lake on the end,\nLook around a boat is there.')
    river = input('Would you like to swim across the river or take the boat? Choose(Swim/Boat)')
    if (river =="Swim"):
        print("The River is crossed successfully, you find the pot of treasure")
    elif (river =="Boat"):
        print("There is a hole in the boat, you are sinking to the water....")
        print("Game Over........................")
    else:
        print("Invalid Entry, Start again...")
elif crossRoad == "R":
    print('You have choosen Left, Walked for few minutes. You find a wall on the end.')
    #print("Would you like to climb up the wall or dig under the wall")
    wall = input('Would you like to climb up the wall or dig under the wall? Choose(Climb/Dig)')
    if (wall =="Climb"):
        print("The Wall is crossed successfully, you find the pot of treasure")
    elif (wall =="Dig"):
        print("There is a snake well under the wall, you are dead....")
        print("Game Over........................")
    else:
        print("Invalid Entry, Start again...")
else:
    print("Invalid Entry, Start again...")



