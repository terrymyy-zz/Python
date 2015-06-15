globvar = 0

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def set_globvar_to_two():
    global globvar
    globvar = 2

def print_globvar():
    globvar = 0
    print globvar     # No need for global declaration to read value of globvar

set_globvar_to_one()
set_globvar_to_two()
print_globvar()       # Prints 1
