import classes
from classes.SquadFunction import SquadFunction
squadFunctions =  { 
"squad" : SquadFunction("Entire Squad","Refers to the whole squad","squad",""),
"prime" : SquadFunction("Prime (First) Squad Member","Refers to the first member of your squad","prime",""),
"@allsquads" : SquadFunction("The Whole Darn Server","Refers to every player and their squadmates (the whole server)","@allsquads",""),
"nco" : SquadFunction("Non-commissioned Officers","Refers to Non-commissioned officers (Rebel troopers and Stormtroopers)","nco",""),
"friend" : SquadFunction("Close Comrades","Refers to you squad leader friends (players)","friend",""),
"%" : SquadFunction("Good Vs. Evil","Refers to ANY personnel that are on the side you specified (players, Player Soldiers (Squad Members), Pilots, etc.)","%","Good"),
"squad-" : SquadFunction("The TRUE Squad Function","Refers to any personnel within the specified squad id","squad-","1337"),
"faction-" : SquadFunction("Factions","Refers to any personnel whose squad leaders are part of the specified class","faction-","Rebels"),
"-" : SquadFunction("Exclusive","Refers to any squad leader who is NOT the one with the specified Roblox User ID","-","1337"),
"#" : SquadFunction("A Handful of Soldiers","Refers to a randomly selected group of squad members from your squad, limited by the number of members you specify","#","12"),
"radius-" : SquadFunction("Radar","Refers to members of your squad who are within a specified distance (in studs) of you, REGARDLESS of direction","radius-","14"),
}

def getSquadFunction(funcName):
   return squadFunctions[funcName]()


