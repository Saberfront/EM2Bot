
availableBlasters = ["A280","A280C","A380","DC15X","DT29","E-11"]

def getBlasterString():
    blasterStr = """**AVAILABLE BLASTERS**: \n ```"""
    for x, blaster in enumerate(availableBlasters):
        blasterStr = blasterStr + str(x) + ". " + blaster + " \n"
    blasterStr = blasterStr + "```"
    return blasterStr

