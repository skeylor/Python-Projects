border = '-'*80


def body_mass_index():
    global height
    while True:
        try:
            #weight = int(input('Enter your weight in lbs: '))
            #type casting weight to an integer.
            #feet,inches = map(int,input('Enter your height in feet and inches: ').split())
            #creates a hash map to store the values seperately.
            weight = 200
            feet = 5
            inches = 10
            height = feet*12 + inches 
            bmi = (weight * 703)/(height**2)
            #formula to calculate bmi with lbs and inches.
            print(border)
            print('weight =',weight)
            print('Your bmi is',bmi)
        except ValueError as error:
            print('Error Code: ',error)
            print('Try that again with a valid input.')
            continue
        
        if bmi < 16:
            print('You need to gain some weight asap!!')
        elif 16 <= bmi < 18.5:
            print('You should gain some weight')
        elif 18.5 <= bmi < 25:
            print('Maintain your weight.')
        elif 25 <= bmi < 30:
            print('You should lose some weight')
        elif bmi >= 30:
            print('You need to lose some weight asap!!')
        else:
            print('That is not a valid input, try again.')
        
        return bmi
       
bmi = body_mass_index()

def gain_or_loss(b):
    weight = (b * (height**2))/703
    weight = round(weight)
    original_weight = weight
    print('weight =',weight)
    print('original weight =',original_weight)
    gain = 0
    loss = 0
    if b > 25:
        while b > 25:
            loss -= .1
            weight += loss
            b = (weight * 703)/(height**2)
        difference = original_weight - weight
        print('weight =',weight)
        print('original weight =',original_weight)
        print('difference =',difference)
        print('You need to lose',round(difference),'lbs. to be at a healthy weight.')
    else:
        while b <= 18.5:
            gain += .1
            weight += gain
            b = (weight * 703)/(height**2)
        difference = abs(original_weight - weight)
        print('You need to gain',round(difference),'lbs. to be at a healthy weight.')
    print('You should shoot for a weight of',round(weight))
    
    return difference
                    
gain_or_loss(bmi)
    