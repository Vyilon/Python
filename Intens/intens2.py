import random

i = 0
win = 0
while i < 1000:

    def monty_hol_paradox(first_door, change):
        global win
        doors_number_list = [1, 2, 3]
        door_with_gift = random.randrange(1, 4)
        door_for_change_list = doors_number_list.copy()
        door_for_change_list.remove(first_door)
        if change:
            if door_with_gift in door_for_change_list:
                win += 1
            else:
                pass
        else:
            if first_door == door_with_gift:
                win += 1
            else:
                pass


    first_door = random.randrange(1, 4)
    door_change = 1 #1-True 0 - False
    result = monty_hol_paradox(first_door, door_change)
    print(win)
    i+=1
