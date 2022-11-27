"""
#Calculating Watt's law
def power(v, i):
    power = v * i
    print ('The amount of power is',power,'W.')

def volts(p, i):
    volts = p/i
    print ('The amounts of volts is',volts,'V.')
    
def current(p, v):
    current = p/v
    print ('The amount of current is',current,'amps.')
    
def watts_law(p,i,v):
    unit = input('Type (P)to solve for power in Watts, type (I)to solve for current in amperes, or type (V)to solve for voltage.')
    if unit.upper() == 'P':
        I = float(input('I:'))
        V = float(input('V:'))
        converted = I * V
        print('Power in watts is',converted)
elif unit.upper() == 'I':
    P = float(input('P:'))
    V = float(input('V:'))
    converted = P/V
    print('Current in amperes is', converted)
elif unit.upper() == 'V':
    P = float(input('P:'))
    I = float(input('I:'))
    converted = P/I
    print('Voltage is',converted)
    

""" #Ohm's law/Watt's law

def ohms_law():
    unit = input('Type(P)for Watts, type(I)for current, type(V)for volts, type(R)for resistance')
    if unit.upper() == 'P': #The .upper method automatically converts the user input to an uppercase letter.
        I = float(input('I:'))
        V = float(input('V:'))
        converted = I * V    #The formula for power is P = I * V
        print('Power in watts is' ,converted)
    elif unit.upper() == 'I':   
        P = float(input('P:'))
        V = float(input('V:'))
        converted = P/V          #The formula for current is I = P/V
        print('Current in amperes is', converted)
    elif unit.upper() == 'V':   
        P = float(input('P:'))
        I = float(input('I:'))
        converted = P/I          #The formula for volts is V = P/I
        print('Voltage is',converted)
    elif unit.upper() == 'R':
        V = float(input('V:'))
        I = float(input('I:'))
        converted = V/I          #The formula for resistance is R = V/I
        print('Resistance is',converted)
    
ohms_law()