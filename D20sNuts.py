init_mods = {
    "Keegan":-1,
    "Matt":3,
    "Dave":2,
    "Kenny":4,
    "Taylor":2,
    "JD":2,
    "Will":0,
    "Tristan":3}
attendance = {}
def start_of_session():
    print()
    print("Type '1' for Yes, '0' for No")
    for i in (init_mods):
        attendance[i] = int(input('Is '+i+" here? "))
    print("Attendance:",attendance)
    start_of_battle()
def start_of_battle(): 
    print()
    print("New Battle Start")
    print()
    enemy_number = int((input("How many enemy units are we fighting? ")))
    friendly_number = int((input("How many friendly combatants? ")))
    print()
    start_of_round(enemy_number,friendly_number)
def start_of_round(x,y):
    enemy_inits = {} 
    friendly_inits = {}  
    player_inits = {} 
    enemy_number = x
    friendly_number = y
    for i in range(1,enemy_number+1):
        j = f"Enemy {i}"
        enemy_inits.update({j:int(input(j+"'s total initiative: "))})
    if enemy_number > 0:
        print()    
    for i in range(1,friendly_number+1):
        j = f"Friendly {i}"
        friendly_inits.update({j:int(input(j+"'s total initiative: "))})
    if friendly_number > 0:
        print()    
    for i in (attendance):
        if attendance[i] == 1:
            player_inits[i] = int(input("What's "+i+"'s roll? "))
            if player_inits[i] == 20:
                player_inits[i] = 100
            if player_inits[i] == 1:
                player_inits[i] = -100 
            player_inits[i] = int(player_inits[i]) + int(init_mods[i])
    print()
    full_inits = merge(enemy_inits,player_inits,friendly_inits)
    print("Initiative totals: ")
    print(full_inits)
    print()
    print("Initiative Order: ")
    for i in sorted(full_inits,key=full_inits.get,reverse=True):
        print(i)
    print()
    if int(input("Type '1' for another round, or '0' for next battle. ")) > 0:
        print("NEW ROUND START")
        print()
        start_of_round(enemy_number,friendly_number)
    else:
        start_of_battle()
def merge(dict1, dict2, dict3):
    res = {**dict1, **dict2, **dict3}
    return res  
start_of_session()
#nice!
#compare crit fails and crit hits from friendly/enemy? cant do that without roll/mod calc.