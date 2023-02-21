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
friendly_mod = {}
enemy_mod = {}
enemy_crits = {}
friendly_crits = {}
def start_of_session():
    print()
    print("Type '1' for Yes, '0' for No")
    for i in (init_mods):
        attendance[i] = int(input('Is '+i+" here? "))
    print("Attendance:",attendance)
    print()
    which_functionality = int(input("Do you want to enter NPC/Enemy Dex Mod Values(enter:1) or just sort total initiative scores(enter:0) "))
    start_of_battle(which_functionality)
def start_of_battle(which_functionality): 
    print()
    print("New Battle Start")
    print()
    enemy_number = int((input("How many enemy units are we fighting? ")))
    for i in range(1,enemy_number+1):
        if which_functionality:
            enemy_mod[i] = input(f"Enemy {i} initiative mod? ")
        else:
            enemy_mod[i] = '0'
    print()        
    friendly_number = int((input("How many friendly NPC combatants? ")))
    for i in range(1,friendly_number+1):
        if which_functionality:
            friendly_mod[i] = input(f"Friendly {i} initiative mod? ")
        else:
            friendly_mod[i] = '0'
    print()
    start_of_round(enemy_number,friendly_number,enemy_mod,friendly_mod,which_functionality)
def start_of_round(a,b,c,d,e): 
    player_inits = {} 
    enemy_number = a
    friendly_number = b
    enemy_mod = c
    friendly_mod = d
    which_functionality = e
    enemy_inits = {}
    friendly_inits = {}
    for i in range(1,enemy_number+1):
        j = f"Enemy {i}"
        enemy_inits.update({j:'0'})
        enemy_mod.update({j:enemy_mod[i]})
    for i in range(1,friendly_number+1):
        k = f"Friendly {i}"
        friendly_inits.update({k:'0'})
        friendly_mod.update({k:friendly_mod[i]})        
    for i in enemy_inits:
        if which_functionality:
            enemy_inits[i] = int(input(i+"'s initiative roll: "))
            if enemy_inits[i] == 20:
                enemy_inits[i] = 100
            if enemy_inits[i] == 1:
                enemy_inits[i] = -100 
        else:
            enemy_inits[i] = int(input(i+"'s total initiative: "))
            if enemy_inits[i] > 19:
                enemy_crits[i] = int(input("1=yes, 2=no - Was this a crit? "))
                if enemy_crits[i]:
                    enemy_inits[i] = 'CRIT!'
        enemy_inits[i] = int(enemy_inits[i]) + int(enemy_mod[i])
    if enemy_number > 0:
        print()    
    for i in friendly_inits:
        if which_functionality:
            friendly_inits[i] = int(input(i+"'s initiative roll: "))
            if friendly_inits[i] == 20:
                friendly_inits[i] = 100
            if friendly_inits[i] == 1:
                friendly_inits[i] = -100 
        else:
            friendly_inits[i] = int(input(i+"'s total initiative: "))
        friendly_inits[i] = int(friendly_inits[i]) + int(friendly_mod[i])
    if friendly_number > 0:
        print()    
    for i in (attendance):
        if attendance[i] == 1:
            if which_functionality:
                player_inits[i] = int(input("What's "+i+"'s roll? "))
                if player_inits[i] == 20:
                    player_inits[i] = 100
                if player_inits[i] == 1:
                    player_inits[i] = -100 
            else: 
                player_inits[i] = int(input("What's "+i+"'s total initiative? "))   
            if which_functionality:
                player_inits[i] = int(player_inits[i]) + int(init_mods[i])
    print()
    full_inits = merge(enemy_inits,player_inits,friendly_inits)
    print("Initiative Order: ")
    for i in sorted(full_inits,key=full_inits.get,reverse=True):
        print(i, ":",full_inits[i])
    print()
    if int(input("Type '1' for another battle with same enemy/friendly NPC setup, or '0' for next battle. ")) > 0:
        print("NEW FIGHT START")
        print()
        start_of_round(enemy_number,friendly_number,c,d,e)
    else:
        start_of_battle(e)
def merge(dict1, dict2, dict3):
    res = {**dict1, **dict2, **dict3}
    return res  
start_of_session()