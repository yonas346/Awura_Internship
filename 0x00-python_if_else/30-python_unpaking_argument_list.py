def parrot(voltage, state='a stiff', action='voom'):
    print("-- this parrot wouldn't ", action, end=' ')
    print("if you put",voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d ={"voltage": "four million", "state": "bleedin' deminsed", "action": "voom"}
parrot(**d)