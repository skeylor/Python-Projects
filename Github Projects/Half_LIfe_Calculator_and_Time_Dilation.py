import math,time
border = '_' * 100


def half_life():
    print('Half-life Calculator')
    print(border)
    print('You will be prompted for the unit separately.')
    print('Just enter the name or quantity of the substance.\n')
    substance = input('Enter the name of the substance: ')
    initial_mass = float(input('Enter the inital mass of the substance: '))
    target_mass = float(input('Enter the ending mass of the substance: '))
    unit_mass = input('Enter the unit of mass: ')
    half_life = float(input('Enter the half-life of the substance: '))
    unit_mass_time = input('Enter the unit of time: ')
    print('Half-life for',substance,':',initial_mass,unit_mass,'to',target_mass,unit_mass)
    # num is storing a variable that can be incremented to store the time that has elapsed.
    num = 0
    half_lives_counter = 0
    print('\n'*10)
    print(border)
    print()
    print('Half-lives Elapsed',end=(''.center(10)))
    print('Time elapsed'+'('+unit_mass_time+')',end=(''.center(10)))
    print(substance,'amount'+'(',unit_mass,')')
    print(border)
    print()
    # The while loop will continue to loop through and iterate until the condition has been met.
    while initial_mass > target_mass:
        num += 1
        half_lives_counter += 1
        initial_mass = initial_mass/2
        time_elapsed = half_life * num
        # ljust is a method for strings that stands for left justified.
        # This method is useful for getting 
        print(''.ljust(5),str(num).ljust(30),end=(''))
        print(str(time_elapsed).ljust(30),end=(''))
        print(str(initial_mass).ljust(5))
    print('Total time = ',time_elapsed)
    
#half_life()
        


'''
Tobserver = time that passes from stationary observer's frame (Earth)
Ttraveler = time that passes for a traveler (spaceship)
p = the percentage of light speed as a decimal
time dilation = Tobserver/Ttraveler
Tobserver = (Ttraveler)/(math.sqrt(1 - p**2)

'''
def time_dilation():
    print('Welcome to the time dilation table.')
    print()
    print(border)
    print()
    print('Enter all values without units')
    print('You will be prompted for units separately \n')
    travel_time = float(input('Enter the length of interstellar travel time: '))
    unit_time = input('Enter the unit of time: ')
    percent_light_speed = (int(input('Enter the light speed as a percentage:')))
    print(border)
    print()
    print('Percent of Light Speed',end=(''.center(10)))
    print('Travel Time',end=(''.center(10)))
    print('Time Dilation',end=(''.center(10)))
    print('Earth Time')
    print(border)
    print()
    while percent_light_speed < 100:
        decimal_light_speed = percent_light_speed/100
        dilation = (math.sqrt(1 - decimal_light_speed**2))
        earth_time = travel_time/dilation
        time_dilation = round((earth_time/travel_time),2)
        print(''.ljust(1),f'{percent_light_speed}% light speed'.ljust(20),end=(''))
        print(''.ljust(10),str(travel_time),unit_time.ljust(17),end=(''))
        print('{:<.2f}'.format(time_dilation),''.ljust(15),end=(''))
        print(round(earth_time,2),unit_time.center(5))
        if percent_light_speed < 80:
            percent_light_speed += 10
        else:
            percent_light_speed += 1
            

def calculator_menu():
    print('Physics Calculator Menu')
    print()
    print(border)
    print()
    print('Choose from one of the following:')
    print('1. Calculate a half-life/substance decay table.')
    print('2. Calculate a time dilation table.')
    print('3. Quit.')
    answer = input('Enter the number of your choice: ')
    if answer == '1':
        half_life()
    elif answer == '2':
        time_dilation()
    elif answer == '3':
        print('Okay, bye!!')
        time.sleep(2)
        quit()
    else:
        print()
        print('Invalid input...  Try again')
        time.sleep(2)
        calculator_menu()

calculator_menu()
            
    
    


    
    