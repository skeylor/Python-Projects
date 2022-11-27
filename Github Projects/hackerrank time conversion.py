import re


s = '12:00:00am'


def timeConversion(s):
    s = s.split(':')
    if 'PM' in s[2].upper():
        s[0] = int(s[0])
        if s[0] == 12:
            pass
        else:
            s[0] = int(s[0])
            s[0] += 12
    elif 'AM' in s[2].upper():
        s[0] = int(s[0])
        if s[0] < 10:
            s[0] = str(s[0]).zfill(2)
        elif s[0] == 12:
            s[0] -= 12
            s[0] = str(s[0]).zfill(2)
        else:
            pass
    s[0] = str(s[0])
    s = ':'.join(s)
    s= s[:-2]
    return s
 
        
print(timeConversion(s))
       


    
