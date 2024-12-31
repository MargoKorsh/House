room_list = []
#Enter #0
enter = ["This is the doorstep. Guards 💂 are letting you in", 2, None, None, None]
room_list.append(enter)
 
#Sport Hall West #1
sport_hall = ["This is a Sports Hall (West). You can only play soccer ⚽ in here ", 4, 2, None, None]
room_list.append(sport_hall)
 
#Sports Hall East #2
room = ["This is a Sports Hall (East). You can play 🏐 and 🏀", 5, 3, 0, 1]
room_list.append(room)
 
#Swimming Pool #3
swimming_pool = ["This is a Swimming Pool. You can 🏊 here. But don't forget to wear 🩱", 
None, #north
None, #east
None, #south
2] #west
room_list.append(swimming_pool)
 
#Playing Room #4
playing_room = ["This is Playing Room. Enjoy ur time 🎮", 7, 5, 1, None]
room_list.append(playing_room)
 
#Bathroom #5
bathroom = ["This is Bathroom. Only do 💩 in this room", 8, 6, 2, 4]
room_list.append(bathroom)
 
#Balcony 1 #6
balcony_1 = ["This is Balcony 1. Breath 🌬️", 9, None, 3, 5]
room_list.append(balcony_1)
 
#Kitchen #7
kitchen = ["This is Kitchen. Eat 🍦 to make 👻 happy", 10, 8, 4, None]
room_list.append(kitchen)
 
#South Hall #8
south_hall = ["This is South Hall", 11, 9, 5, 7]
room_list.append(south_hall)
 
#Dining Hall #9
dining_hall = ["This is Dining Hall. Enjoy 🥧 with ☕", None, None, 6, 8]
room_list.append(dining_hall)
 
#Bedroom 1 #10
bedroom_1 = ["This is Bedroom 1. Get some 💤", 13, 11, 7, None]
room_list.append(bedroom_1)
 
#North Hall #11
north_hall = ["This is North Hall", None, 12, 8, 10]
room_list.append(north_hall)
 
#Bedroom 2 #12
bedroom_2 = ["This is Bedroom 2. Lay on 🛏️", 13, None, None, 11]
room_list.append(bedroom_2)
 
#Balcony 2 #13
balcony_2 = ["This is Big Balcony. Look at 🌇", None, None, 11, None]
room_list.append(balcony_2)
 
current_room = 0
 
done = False
while not done:
    print()
    print(room_list[current_room][0])
    move = input("Which direction you want to move? N, E, S, or W?")
    #North
    if move.upper() == "N":
        next_room = room_list[current_room][1] #north
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    #East
    elif move.upper() == "E":
        next_room = room_list[current_room][2] #east
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    #South
    elif move.upper() == "S":
        next_room = room_list[current_room][3] #south
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    #West
    elif move.upper() == "W":
        next_room = room_list[current_room][4] #west
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
