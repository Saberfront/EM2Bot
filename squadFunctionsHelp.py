

squadFunctions =  { 
"squad" : "Refers to the whole squad",
"prime" : "Refers to the first member of your squad",
"@allsquads" : "Refers to every player and their squadmates (the whole server)",
"nco" : "Refers to Non-commissioned officers (Rebel troopers and Stormtroopers)",
"friend" : "Refers to you squad leader friends (players)",
"%" : "Refers to ANY personnel that are on your side (players, Player Soldiers (Squad Members), Pilots, etc.)",




}

def getSquadFunction(funcName):
   return squadFunctions[funcName]


