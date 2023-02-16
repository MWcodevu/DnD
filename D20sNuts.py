init_mods = {
    "Keegan":-1,
    "Matt":3,
    "Dave":2,
    "Kenny":4,
    "Taylor":2,
    "JD":2,
    "Will":0,
    "Tristan":3}
attendance = {
    "Keegan":1,
    "Matt":1,
    "Dave":1,
    "Kenny":1,
    "Taylor":1,
    "JD":1,
    "Will":1,
    "Tristan":1}
last_roll = {
    "Keegan":1,
    "Matt":1,
    "Dave":1,
    "Kenny":1,
    "Taylor":1,
    "JD":1,
    "Will":1,
    "Tristan":1}
current_inits = {
    "Keegan":1,
    "Matt":1,
    "Dave":1,
    "Kenny":1,
    "Taylor":1,
    "JD":1,
    "Will":1,
    "Tristan":1}
init_order = {
    "Keegan":1,
    "Matt":1,
    "Dave":1,
    "Kenny":1,
    "Taylor":1,
    "JD":1,
    "Will":1,
    "Tristan":1} 
enemy_inits = {} 
friendly_inits = {}  
def start_of_session():
    print("Type '1' for Yes, '0' for No")
    for i in (attendance):
        attendance[i] = int(input('Is '+i+" here? "))
    print("Attendance:",attendance)
    start_of_battle()
def start_of_battle():
    print()
    print("Start of Battle")
    print()
    enemy_number = int((input("How many enemy units are we fighting? ")))
    friendly_number = int((input("How many friendly combatants? ")))
    print()
    start_of_round(enemy_number,friendly_number)
def start_of_round(x,y):
    enemy_number = x
    friendly_number = y
    for i in range(1,enemy_number+1):
        print("Enemy",i,":")
        j = f"Enemy {i}"
        enemy_inits.update({j:int(input("Enemy's init: "))})
    print()
    for i in range(1,friendly_number+1):
        print("Friendly",i,":")
        j = f"Friendly {i}"
        friendly_inits.update({j:int(input("Friendly's init: "))})
    if friendly_number > 0:
        print()
    for i in (last_roll):
        last_roll[i] = int(input("What's "+i+"'s roll? "))
        if last_roll[i] == 20:
            last_roll[i] = 100
        if last_roll[i] == 1:
            last_roll[i] = -100    
    for i in (current_inits):
        current_inits[i] = int(last_roll[i]) + int(init_mods[i])
    print()
    full_inits = merge(enemy_inits,current_inits,friendly_inits)
    print("All Rolls: ",full_inits)
    print("Initiative Order: ",sorted(full_inits,key=full_inits.get,reverse=True))
    print()
    goagain = int(input("Type '1' for another round, or '0' for next battle. "))
    if goagain > 0:
        print("NEW ROUND START")
        print()
        start_of_round(enemy_number,friendly_number)
    else:
        start_of_battle()
def merge(dict1, dict2,dict3):
    res = {**dict1, **dict2, **dict3}
    return res  
start_of_session()