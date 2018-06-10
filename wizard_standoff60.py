from random import randint

class Wizard:
    def __init__(self, chance, initiative):
        self.chance = chance
        self.initiative = initiative
        self.dead = False
    
    def target(self, wizardlist):
        if dead_counter == 1:
            for wizard in wizardlist:
                if wizard.initiative != self.initiative and wizard.dead == False:
                    print("Wizard " + str(self.initiative) + " targets Wizard " + str(wizard.initiative) + "...")
                    target = wizard.initiative
                    return target
                else:
                    continue
        else:
            if strongest_wizard(wizardlist) == self.initiative:
                if wizardlist[0].initiative != self.initiative:
                    wizard1 = wizardlist[0]
                    if wizardlist[1].initiative != self.initiative:
                        wizard2 = wizardlist[1]
                    else:
                        wizard2 = wizardlist[2]
                else:
                    wizard1 = wizardlist[1]
                    wizard2 = wizardlist[2]
                    
                target = which_one_is_stronger(wizard1, wizard2)
                    
                print("Wizard " + str(self.initiative) + " targets Wizard " + str(target) + "...")
                return target

            elif middle_wizard(wizardlist) == self.initiative:
                target = strongest_wizard(wizardlist)
                return target
            else:
                print("Wizard " + str(self.initiative) + " misses purposefully!")
                return None

    
    def shoot(self, target, wizardlist):
        for wizard in wizardlist:
            if target == wizard.initiative:
                print("Wizard " + str(self.initiative) + " shoots Wizard " + str(wizard.initiative) + "!")
                chance = randint(1, 100)
                print("Chance to die: " + str(self.chance) + "%")
                print("Roll: " + str(chance))
                if chance <= self.chance:
                    print("Wizard " + str(wizard.initiative) + " dies!")
                    wizard.dead = True
                    return True
                else:
                    print("Wizard " + str(wizard.initiative) + " survives!")
                    return False
            else:
                continue

def strongest_wizard(wizardlist):
    if wizardlist[0].chance > wizardlist[1].chance:
        if wizardlist[0].chance > wizardlist[2].chance:
            return wizardlist[0].initiative
        else:
            return wizardlist[2].initiative
    elif wizardlist[1].chance > wizardlist[2].chance:
        return wizardlist[1].initiative
    else:
        return wizardlist[2].initiative

def middle_wizard(wizardlist):
    if wizardlist[0].chance > wizardlist[1].chance:
        if wizardlist[2].chance > wizardlist[0].chance:
            return wizardlist[0].initiative
        else:
            if wizardlist[1].chance > wizardlist[2].chance:
                return wizardlist[1].initiative
            else:
                return wizardlist[2].initiative
    else:
        if wizardlist[2].chance > wizardlist[1].chance:
            return wizardlist[1].initiative
        else:
            if wizardlist[0].chance > wizardlist[2].chance:
                return wizardlist[0].initiative
            else:
                return wizardlist[2].initiative
                
def which_one_is_stronger(wizard1, wizard2):
    if wizard1.chance > wizard2.chance:
        return wizard1.initiative
    else:
        return wizard2.initiative
        
def update_wizardlist(wizardlist):
    new_wizardlist = []
    for wizard in wizardlist:
        if wizard.dead == False:
            new_wizardlist.append(wizard)
    wizardlist = new_wizardlist
    return wizardlist

def start_round(wizardlist):
    global dead_counter
    for wizard in wizardlist:
        if wizard.dead == False:
            target = wizard.target(wizardlist)
            if target != None:
                if wizard.shoot(target, wizardlist) == True:
                    dead_counter += 1
            print("")
    update_wizardlist(wizardlist)

def check_first_round(wizardlist):
    if dead_counter == 0:
        for wizard in wizardlist:
            wizard.dead = True
        print("Everyone died, nobody won!")
        return False
    else:
        return True

def create_wizardlist():
    wizardlist = []
    
    wizardlist.append(Wizard(60, 0))
    wizardlist.append(Wizard(70, 1))
    wizardlist.append(Wizard(90, 2))

    return(wizardlist)

def tell_stats(wizardlist):
    for wizard in wizardlist:
        print("Wizard " + str(wizard.initiative) + ": the " + str(wizard.chance) + "% wand")    

def determine_winner(wizardlist):
    for wizard in wizardlist:
        if wizard.dead == False:
            print("Wizard " + str(wizard.initiative) + " wins!")

def main_loop():
    wizardlist = create_wizardlist()
    tell_stats(wizardlist)
    print("")
    start_round(wizardlist)
    if check_first_round(wizardlist) == True:
        while dead_counter != 2:
            start_round(wizardlist)
            

    determine_winner(wizardlist)

dead_counter = 0
main_loop()
