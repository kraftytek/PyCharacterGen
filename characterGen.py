#Made by Kraftytek
import random

#roll functions 

def roll_stat():
    roll = random.randint(3, 18)
    return roll
    
def roll_D6():
        roll = random.randint(1, 6)
        return roll
        
def complete_stat():        
        
        stat_roll = [roll_D6(), roll_D6(), roll_D6(), roll_D6()]
        allRoll = sum(stat_roll)
        lowest = min(stat_roll)
        total = int(allRoll) - int(lowest)
        return total
        
#content arrays        

fnameList = ["Terry", "Phil", "Nick", "Tyson", "Jenny", "Barry", "Ebbers", "Mark", "Dave", "Amanda", "Clark",
             "Stan", "Gina", "Hank", "Crunt", "Felix", "Johnson", " Angeluh", "Fook", "Ryan", "Gloin", "Rasher"
             "Flint", "Frank", "Craig"]
             
lnameList = ["Uppermuffin", "Hardlove", "Buttermaker", "Fingerlicking", "Rubberboot", "Hardchair", "Shoebreaker",
             "Feelgood", "Hooter", "Prunt", "Sizzlecock", "Strumpletin", "Duh", "Nood"]
             
raceList = ["Elf", "Human", "Dwarf", "Drow", "Gnome", "Orc", "Half elf", "Half Orc"]

feats = ["Actor", "Alert", "Artificer Initiate", "Athlete", " Boutiful Luck", "Charger", "Chef", "Crossbow Expert",
         "Crusher", "Defensive Duelist", "Dragon Fear", "Dragon Hide", "Dual Wielder", "Dungeon Delver", "Durable",
         "Dwarf Fortitude", "Eldritch Adept", "Elemental Adept", "Elven Accuracy", "Fade Away", "Fey Touched", "Healer",
         "Keen Mind", "Lightly Armored"]

charClass = ["Warrior", "Paladin", "Rogue", "Mage", "Bard", "Cleric", "Sorcerer", "Ranger", "Druid"]

charQuirk = ["Limp", "Shakes", "Very Short", "Blind", "Annoying", "Loud Eater", "Missing Left Eye", "Missing Right Eye",
             "Missing Left Leg", "Missing Right Leg", "Missing Left Arm", "Missing Right Arm", "Ugly", "A.D.D."]
             
#prep rolls for character generation             

fnameRoll = random.randint(0, len(fnameList) - 1)
lnameRoll = random.randint(0, len(lnameList) - 1)
raceRoll = random.randint(0, len(raceList) - 1)
classRoll = random.randint(0, len(charClass) - 1)
quirkRoll = random.randint(0, len(charQuirk) - 1)
featRoll = random.randint(0, len(feats) - 1)
fname = fnameList[fnameRoll]
lname = lnameList[lnameRoll]
cClass = charClass[classRoll]
cQuirk = charQuirk[quirkRoll]
cFeat = feats[featRoll]
strength = complete_stat()
dex = complete_stat()
intelligence = complete_stat()
constitution = complete_stat()
wisdom = complete_stat()
luck = complete_stat()
race = raceList[raceRoll]
level = 1
exp = 0

#build and print string of generated character

print("  \nLevel = " + str(level)
      + "\nName = " + fname + " " + lname
      + "\nClass = " + cClass 
      + "\nQuirk = " + cQuirk
      + "\nFeat = " + cFeat
      + "\nRace = " + race
      + "\nHP = " + str(constitution * 6)
      + "\nStrength = " + str(strength)
      + "\nDex = " + str(dex)
      + "\nIntelligence = " + str(intelligence)
      + "\nConstitution = " + str(constitution)
      + "\nWisdom = " + str(wisdom)
      + "\nluck = " + str(luck)
      )
