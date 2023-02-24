def functionality():
    print("\nDee 20's Nuts\n")
    print("How do you want this to work?")
    print("(1) Prompts for enemy/friendlyNPC dex mods & rolls, calculates initiative, recognizes crits/fails, resolves ties")
    print("(0) Prompts for total initiative scores and sorts high to low. No logic for crits/fails or ties")
    which_functionality = -1
    while which_functionality != 1 and which_functionality != 0:
        try:
            which_functionality = int(input("Choose 1 or 0: "))
            if which_functionality > 1 or which_functionality < 0:
                x=int("") #meant to fail
        except:
            print("Invalid Entry. Try again") 
    return which_functionality
def attendance():
    print()
    player_mods = { 
    "Keegan":-1,
    "Matt":3,
    "Dave":2,
    "Kenny":4,
    "Taylor":2,
    "J.D.":2,
    "Will":0,
    "Tristan":3    
    }
    roster = {}
    present = {}
    print("Attendance: Answer 1 for present, 0 for absent")
    for i in (player_mods):
        roster[i] = -1
        while roster[i] !=1 and roster[i] !=0:
            try:
                roster[i] = int(input('Is '+i+" here? "))
                if roster[i] > 1 or roster[i] < 0:
                    x=int("") #meant to fail
            except:
                print("Invalid Entry. Try again")    
        if roster[i] == 1:
            present[i] = player_mods[i]
    print(f"Dex mods for those in attendance: {present}")        
    return present
def enemy_setup(funct):
    print()
    enemy_number = -1
    while enemy_number < 0:
        try:
            enemy_number = int(input("How many enemy units are we fighting? "))
            if enemy_number < 0:
                x=int("")
        except:
            print("Invalid Entry. Try again")
    if funct:
        if enemy_number > 0:
            print()
    enemy_mods = {}
    for i in range(1,enemy_number+1):
        j = f"Enemy{i}"
        if funct:
            entry = None
            while entry is None:
                try:
                    entry = int(input(f"Enemy{i}'s initiative modifier (dex mod): "))
                except:
                    print("Invalid Entry. Try again")
            enemy_mods.update({j:entry})
        else:
            enemy_mods.update({j:0})           
    return enemy_mods
def friendly_setup(funct):
    print()
    friendly_number = -1
    while friendly_number < 0:
        try:
            friendly_number = int(input("How many friendly NPCs are fighting with the party? "))
            if friendly_number < 0:
                x=int("")
        except:
            print("Invalid Entry. Try again")
    if funct:
        if friendly_number > 0:
            print()
    friendly_mods = {}
    for i in range(1,friendly_number+1):
        j = f"Friendly{i}"
        if funct:
            entry = None
            while entry is None:
                try:
                    entry = int(input(f"Friendly{i}'s initiative modifier (dex mod): "))
                except:
                    print("Invalid Entry. Try again")
            friendly_mods.update({j:entry}) 
        else:
            friendly_mods.update({j:0})              
    return friendly_mods
def rolls(enemy_mods,friendly_mods,player_mods,funct):
    print("\nRoll for initiative!\n")
    all_rolls = {}
    all_mods = {**enemy_mods,**friendly_mods,**player_mods}
    for i in (all_mods):
        if funct:
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
            if all_rolls[i] == 20:
                all_rolls[i] = 100
            elif all_rolls[i] == 1:
                all_rolls[i] = -100
        else:
            entry = None
            while entry is None:
                try:
                    entry = int(input(f"What is {i}'s total initiative? "))
                except:
                    print("Invalid Entry. Try again")
            all_rolls.update({i:entry})        
    return all_rolls
def addmods(enemy_mods,friendly_mods,player_mods,allrolls,funct):
    all_mods = {**enemy_mods,**friendly_mods,**player_mods}
    total_initiatives = {}
    for i in all_mods:
        if funct:
            total_initiatives[i] = allrolls[i] + all_mods[i] * 1.01
        else:
            total_initiatives[i] = allrolls[i]
    return total_initiatives    
def crits(initiatives,funct):
    crit_hits = {}
    crit_fails = {}
    non_criticals = {}
    for i in initiatives:
        if funct:
            if initiatives[i] > 50:
                crit_hits[i] = initiatives[i]
            elif initiatives[i] < -50:
                crit_fails[i] = initiatives[i]
            else:
                non_criticals[i] = initiatives[i]
    return crit_hits,non_criticals,crit_fails
def tiebreaker(critical_hits,norm_rolls,critical_fails,funct):
    if funct:
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
                        tie_score[t] = None
                        while tie_score[t] is None:
                            try:
                                tie_score[t] = int(input(f"{t} roll for tiebreaker: "))
                                if tie_score[t] > 20 or tie_score[t] < 1:
                                    x=int("")
                            except:
                                print("Invalid Entry. Try again")
                                tie_score[t] = None
                        p[t] = tied_partys[t] + tie_score[t] * 0.0001 
            if len(tied_partys) < 1:
                keep_going = 0
    else:
        tie_score = {}                             
    return critical_hits,norm_rolls,critical_fails,tie_score
def output(critical_hits,norm_rolls,critical_fails,initiatives,funct,pl_mods,en_mods,fr_mods,tie_score):
    space = " "
    mod = {**pl_mods,**en_mods,**fr_mods}
    if funct:
        print("\niOrder :   iTotal  iMod  iTiebreaker  C/F")
        for x in (critical_hits,norm_rolls,critical_fails):
            for i in sorted(x,key=x.get,reverse=True):
                if x[i] > 50:
                    x[i] = x[i] - 80
                    note = "Crit!"
                elif x[i] < -50:
                    x[i] = x[i] + 80
                    note = "Fail!"
                else:
                    note = ""
                try:
                    if tie_score[i] == tie_score[i]:
                        tie_score[i] = tie_score[i]
                except:
                    tie_score[i] = " "
                if round(x[i]) < 0:
                    s1=0
                else:
                    s1=1    
                if mod[i] < 0:
                    s2=0
                else:
                    s2=1  
                space1=space*(10+s1-len(i))
                space2=space*(5+s2-s1-len(str(round(x[i]))))                      
                space3=space*(7-s2-len(str(mod[i])))
                space4=space*(6-len(str(tie_score[i])))
                print(i,f":{space1}",round(x[i]),space2,mod[i],space3,tie_score[i],space4,note)
    else:
        print("\nInitiative Order:")    
        for i in sorted(initiatives,key=initiatives.get,reverse=True):
            if round(initiatives[i]) < 0:
                s1=0
            else:
                s1=1    
            space1=space*(10+s1-len(i))
            print(i,f":{space1}",initiatives[i])
    print()
def do_what_now(funct,pl_mods,en_mods,fr_mods):
    print("OPTIONS:")
    print("0 to restart program")
    print("1 to use SAME players and SAME enemies/friendlyNPCs")
    print("2 to use SAME players -but- NEW enemies/friendlyNPCs")
    print("3 to Exit Program")
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
        execute(where_to_go,funct,pl_mods,en_mods,fr_mods)
    elif where_to_go == 2:    
        execute(where_to_go,funct,pl_mods,-1,-1)
    elif where_to_go == 3:
        print("\nFarewell\n")
        exit()
def execute(where_to_go,funct,pl_mods,en_mods,fr_mods):
    if where_to_go == 0:
        funct = functionality()
        pl_mods = attendance()
    if where_to_go == 2 or where_to_go == 0:
        en_mods = enemy_setup(funct)
        fr_mods = friendly_setup(funct)
    if where_to_go == 2 or where_to_go == 0 or where_to_go == 1:
        rol = rolls(en_mods,fr_mods,pl_mods,funct)
        initiatives = addmods(en_mods,fr_mods,pl_mods,rol,funct)
        critical_hits,norm_rolls,critical_fails = crits(initiatives,funct)
        critical_hits,norm_rolls,critical_fails,tie_score = tiebreaker(critical_hits,norm_rolls,critical_fails,funct)
        output(critical_hits,norm_rolls,critical_fails,initiatives,funct,pl_mods,en_mods,fr_mods,tie_score)
        do_what_now(funct,pl_mods,en_mods,fr_mods)
execute(0,-1,-1,-1,-1)