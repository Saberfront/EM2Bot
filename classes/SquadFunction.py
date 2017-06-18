
class SquadFunction:
    def __init__(self,name,description,syntax,exampleargs):
        self.Name = name
        self.Description = description
        self.Syntax = syntax
        self.Example = ""
        if exampleargs != None and exampleargs != "":
            self.Example = "*" + self.Syntax + exampleargs
        else:
            self.Example = "*" + self.Syntax
    def __str__(self):
        return "**" + self.Name + "** \n *" + self.Syntax + "* : " + self.Description + "\n *Example* : " + self.Example
    def __call__(self):
        return str(self)
        
