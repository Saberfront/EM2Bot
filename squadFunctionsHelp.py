

squadFunctions =  { 
"squad" : "Refers to the whole squad",
"prime" : "Refers to the first member of your squad",
"@allsquads" : "Refers to every player and their squadmates (the whole server)",
"nco" : "Refers to Non-commissioned officers (Rebel troopers and Stormtroopers)",
"friend" : "Refers to you squad leader friends (players)",
"%" : "Refers to ANY personnel that are on your side (players, Player Soldiers (Squad Members), Pilots, etc.)",
"squad-" : "Refers to any personnel within the specified squad id",
"faction-" : "Refers to any personnel whose squad leaders are part of the specified class",
"-" : "Refers to any squad leader who is NOT the one with the specified Roblox User ID",
"#" : "Refers to a randomly selected group of squad members from your squad, limited by the number of members you specify",
"radius-" : "Refers to members of your squad who are within a specified distance of you, REGARDLESS of direction",

}

def getSquadFunction(funcName):
   return squadFunctions[funcName]


