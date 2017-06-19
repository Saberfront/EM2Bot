
availableBlasters = [
    "A280",
    "A280C",
    "A380",
    "DC15X",
    "DT29",
    "E-11",
]

def getBlasterString():
    blasterStr = """**AVAILABLE BLASTERS**: \n ```"""
    for x in availableBlasters:
        blasterStr = blasterStr + x + ". " + availableBlasters[x] + " \n"

    return blasterStr

