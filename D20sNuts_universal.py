def attendance():
    print()
    present = {}
    print("Populating Roster For This Game:\nEnter Player Names.\nDon't reuse names already on your list\nEnter '0' when done.\n")
    adding_player = 1
    while adding_player != '0':
        try:
            adding_player = input("Name of player to add to this game: ")
            if adding_player == "":
                print("Invalid Entry. Try again")  
                x = int("")
            if adding_player != '0':
                while not adding_player in present:
                    try:
                        present[adding_player] = int(input(f"{adding_player} Dex mod: "))
                    except:
                        print("Invalid Entry. Try again")        
            else:
                x=int("")
        except:
            x=1
    print("Dex Mods for current party:")     
    print(present)       
    return present
def enemy_setup():
    print()
    enemy_number = -1
    while enemy_number < 0:
        try:
            enemy_number = int(input("How many enemy units are we fighting? "))
            if enemy_number < 0:
                x=int("")
        except:
            print("Invalid Entry. Try again")
    enemy_mods = {}
    for i in range(1,enemy_number+1):
        j = f"Enemy{i}"
        entry = None
        while entry is None:
            try:
                entry = int(input(f"Enemy{i}'s initiative modifier (dex mod): "))
            except:
                print("Invalid Entry. Try again")
        enemy_mods.update({j:entry})        
    return enemy_mods
def friendly_setup():
    print()
    friendly_number = -1
    while friendly_number < 0:
        try:
            friendly_number = int(input("How many friendly NPCs are fighting with the party? "))
            if friendly_number < 0:
                x=int("")
        except:
            print("Invalid Entry. Try again")
        if friendly_number > 0:
            print()
    friendly_mods = {}
    for i in range(1,friendly_number+1):
        j = f"Friendly{i}"
        entry = None
        while entry is None:
            try:
                entry = int(input(f"Friendly{i}'s initiative modifier (dex mod): "))
            except:
                print("Invalid Entry. Try again")
        friendly_mods.update({j:entry}) 
    return friendly_mods
def rolls(enemy_mods,friendly_mods,player_mods):
    print("\nRoll for initiative!\n")
    all_rolls = {}
    nat_rolls = {}
    all_mods = {**enemy_mods,**friendly_mods,**player_mods}
    for i in (all_mods):
        entry = None
        while entry is None:
            try:
                entry = int(input(f"What did {i} Roll? "))
                if entry > 20 or entry < 1:
                    x=int("")
            except:
                print("Invalid Entry. Try again")
                entry = None
            all_rolls.update({i:entry})
            nat_rolls.update({i:entry})
        if all_rolls[i] == 20:
            all_rolls[i] = 100
        elif all_rolls[i] == 1:
            all_rolls[i] = -100  
    return all_rolls,nat_rolls
def addmods(enemy_mods,friendly_mods,player_mods,allrolls):
    all_mods = {**enemy_mods,**friendly_mods,**player_mods}
    total_initiatives = {}
    for i in all_mods:
            total_initiatives[i] = allrolls[i] + all_mods[i] * 1.01
    return total_initiatives    
def crits(initiatives):
    crit_hits = {}
    crit_fails = {}
    non_criticals = {}
    for i in initiatives:
        if initiatives[i] > 50:
            crit_hits[i] = initiatives[i]
        elif initiatives[i] < -50:
            crit_fails[i] = initiatives[i]
        else:
            non_criticals[i] = initiatives[i] 
    return crit_hits,non_criticals,crit_fails
def tiebreaker(critical_hits,norm_rolls,critical_fails):
    print()
    keep_going = 1
    tie_score = {}
    while keep_going == 1:
        tied_partys = {}
        q = (critical_hits,norm_rolls,critical_fails)
        for p in q:
            for key1,value1 in p.items():
                for key2,value2 in p.items():
                    if value1 == value2 and key1 != key2:
                        if not key2 in tied_partys:
                            tied_partys[key2] = value2
        for p in q:
            for t in tied_partys:
                if t in p:
                    entry = None
                    while entry is None:
                        try:
                            entry = int(input(f"{t} roll for tiebreaker: "))
                            tie_score[t] = entry
                            if entry > 20 or entry < 1:
                                x=int("")
                        except:
                            print("Invalid Entry. Try again")
                            entry = None
                    p[t] = tied_partys[t] + entry * 0.0001 
        if len(tied_partys) < 1:
            keep_going = 0                          
    return critical_hits,norm_rolls,critical_fails,tie_score
def output(critical_hits,norm_rolls,critical_fails,pl_mods,en_mods,fr_mods,tie_score,nat):
    space = " "
    mod = {**pl_mods,**en_mods,**fr_mods}
    print("\niOrder :   iTotal   iRoll    iMod  iTiebreaker  C/F")
    for x in (critical_hits,norm_rolls,critical_fails):
        for i in sorted(x,key=x.get,reverse=True):
            if x[i] > 50:
                x[i] = x[i] - 80
                note = "Crit!"
            elif x[i] < -50:
                x[i] = x[i] + 101
                note = "Fail!"
            else:
                note = ""
            try:
                if tie_score[i] == tie_score[i]:
                    tie_score[i] = tie_score[i]
            except:
                tie_score[i] = " "
            if round(x[i]) < 0:
                iTotalNegative = -1
            else:
                iTotalNegative = 0   
            if mod[i] < 0:
                iModNegative = -1
            else:
                iModNegative = 0
            space1=space*((10+iTotalNegative)-len(i))
            space2=space*((7-iTotalNegative)-len(str(round(x[i])))) 
            space2_5=space*((6+iModNegative)-len(str(nat[i])))                     
            space3=space*((7-iModNegative)-len(str(mod[i])))
            space4=space*(6-len(str(tie_score[i])))
            print(i,f":{space1}",round(x[i]),space2,nat[i],space2_5,mod[i],space3,tie_score[i],space4,note)
def do_what_now(pl_mods,en_mods,fr_mods):
    print("\nOPTIONS:\n0 to restart program\n1 to use SAME players+ SAME enemies/friendlyNPCs\n2 to use SAME players+ NEW enemies/friendlyNPCs\n3 to Exit Program")
    where_to_go = -1
    while where_to_go < 0:
        try:
            where_to_go = int(input("0, 1, 2, or 3. Choose Your Path: "))
            if where_to_go < 0 or where_to_go > 3:
                x=int("")
        except:
            print("Invalid Entry. Try again")
            where_to_go = -1
    if where_to_go == 0:
        execute(where_to_go,-1,-1,-1,-1)
    elif where_to_go == 1:
        execute(where_to_go,pl_mods,en_mods,fr_mods)
    elif where_to_go == 2:    
        execute(where_to_go,pl_mods,-1,-1)
    elif where_to_go == 3:
        print("\nFarewell\n")
        exit()
def execute(where_to_go,pl_mods,en_mods,fr_mods):
    if where_to_go == 0:
        pl_mods = attendance()
    if where_to_go == 2 or where_to_go == 0:
        en_mods = enemy_setup()
        fr_mods = friendly_setup()
    if where_to_go == 2 or where_to_go == 0 or where_to_go == 1:
        rol,nat = rolls(en_mods,fr_mods,pl_mods)
        initiatives = addmods(en_mods,fr_mods,pl_mods,rol)
        critical_hits,norm_rolls,critical_fails = crits(initiatives)
        critical_hits,norm_rolls,critical_fails,tie_score = tiebreaker(critical_hits,norm_rolls,critical_fails)
        output(critical_hits,norm_rolls,critical_fails,pl_mods,en_mods,fr_mods,tie_score,nat)
        do_what_now(pl_mods,en_mods,fr_mods)
execute(0,-1,-1,-1)