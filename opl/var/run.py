vars = []
values = []

def createvar(var, value):
    vars.append(var)
    values.append(value)

def printvar(var):
    print(values[vars.index(var)])

def changevar(var, value):
    values.pop(vars.index(var))
    values.append(value)
