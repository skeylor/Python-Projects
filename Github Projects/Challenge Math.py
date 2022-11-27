from turtle import *
import math
#1.) Physics rate of change challenge

net_fill = 95 - 49

circum = 33

#cirumference = 2*3.14*r

radius = circum/(2*3.14)

print('radius=',radius)

sphere_vol = (4/3)*3.14 * (radius)**3

target_vol = sphere_vol * .85

print('target_vol=',target_vol)

target_vol_liters = target_vol * 1000

print('Target volume in liters = ',target_vol_liters)

capacity = (target_vol_liters/net_fill)/60

print('Capacity =',capacity)

print(20*math.tan(math.pi/10*2.5))

for i in range(5):
    print(i)

#Banker's rounding will always round to the nearest even number
#when the decimal is halfway between two integers (ex. 0.5)
    
print(round(1.5))

print(round(2.5))

print(math.acos(math.tan((5*math.pi)/4)))

height = math.degrees(math.tan(51.8))

print(height)

print(height* 63)

print(math.acos(1))

t = 0

    
    
print(math.sqrt(9/640))

answer = math.acos(0)

print(math.degrees(answer))


'''
1.)The volume of a sphere with radius r is (4/3)pir3.
What is the volume of a sphere with a radius of 5 inches? (Use 3.14 for p.)
'''
def sphere_vol(rad):
    volume = (4/3)*math.pi*rad**3
    volume = round(volume,2)
    print('Sphere volume =',volume,'cubic inches')
    return volume

sphere_vol(5)

'''
2. Suppose the cover price of a book is $24.95,
but bookstores get a 40% discount off that price.
Shipping costs $3 for the first copy and 75 cents
for each additional copy. What is the total wholesale
cost for an order of 60 copies?
'''

def wholesale_cost(books):
    cover_price = 24.95
    discount_price = cover_price - (cover_price *.40)
    shipping_cost = 3 + .75 * (books - 1)
    total_cost = round((discount_price * books + shipping_cost),2)
    print('The total cost of shipping',books,f'books is ${total_cost}')

wholesale_cost(60)


'''
3. Excavation for a pool is being done in your backyard.
It measures 42 ft × 27 ft × 10 ft. The dirt will be taken
away in a truck that holds 540 ft3. How many truckloads
will it take to haul off all the dirt for the excavation?
'''

def excavation(l,w,h):
    volume = l*w*h
    truckload = 540
    excavate = int(volume/truckload)
    print(f'The excavation will take {excavate} truckloads.')
    return excavate

excavation(42,27,10)

'''
4. Ellen can buy bottles of water in packages of 6 for $17.10
or in packages of 4 for $12.20. How much money does she save
by buying 24 bottles of water at the better price?

'''

def better_price():
    six_pack = 17.10
    four_pack = 12.20
    twenty_four_price_6pack = six_pack * 4
    twenty_four_price_4pack = four_pack * 6
    if twenty_four_price_6pack > twenty_four_price_4pack:
        better_price = abs(twenty_four_price_6pack - twenty_four_price_4pack)
        better_price = better_price
        print('The four pack is a better price by ${:<.2f}'.format(better_price))
    else:
        better_price = abs(twenty_four_price_6pack - twenty_four_price_4pack)
        better_price = better_price
        print('The six pack is a better price by ${:<.2f}'.format(better_price))

        
better_price()

'''

5. (Challenge Problem) One leg of a right triangle is 35 cm
and its area is 420 square cm. Find its perimeter.
(Hints: Recall that according to the Pythagorean theorem,
given the lengths of the two sides a and b and the
hypotenuse h: h2 = a2 + b2. And to get the square root
of an expression in Python, you can just raise the expression
to the power ½ using the exponentiation operation, **.)
'''
def right_triangle(base):
    ht()
    #speed(0)
    #delay(0)
    # Area of a square with only the diagonal: A = (1/2)*d**2
    # Area of a right triangle: A = (1/2)*base*height
    # Perimeter of a right triangle: (base + height) + math.sqrt(base**2 + height ** 2)
    # Hypotenuse = math.sqrt(base ** 2 + height ** 2)
    area = 420
    height = (420 * 2)/base
    area = (1/2) * base * height
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    #perimeter = (base + height) + math.sqrt(base**2 + height ** 2)
    # Calculating perimeter without knowing the hypotenuse.
    perimeter = base + height + hypotenuse
    #hypotenuse = math.hypot(base,height)
    # Python has hypotenuse calculator built in :)
    turn = math.asin(height/hypotenuse)
    turn = math.degrees(turn)
    turn = 180 - turn
    final_turn = math.asin(base/hypotenuse)
    final_turn = math.degrees(final_turn)
    final_turn = 180 - final_turn
    fd(base)
    write(base)
    lt(turn)
    fd(hypotenuse)
    write(hypotenuse)
    lt(final_turn)
    fd(height)
    write(height)
    print('Area =',round(area,2))
    print('Perimeter =',round(perimeter,2))
    print('Hypotenuse =',round(hypotenuse,2))
    print('Height =',round(height,2))
    print('Base angle turn =',turn)
    print('Height angle turn =',final_turn)
    
right_triangle(35)
'''
6. (Challenge Problem) Each dimension of a cube has been
increased to twice its original size. If the new cube has
a volume of 216,000 cubic centimeters, what is the area of
one face of the original cube?
'''
# cube volume = edge**3
def cube_vol()
    new_cube_vol = 216000
    new_cube_edge = new_cube_vol**(1/3)
    original_cube_edge = new_cube_edge/2
    original_cube_face_area = original_cube_edge **2
    print('The area of one side of the original cube =',round(original_cube_face_area,2),'cm. squared.')
'''
7. (Challenge Problem) A water tank has the shape of a
rectangular prism of base 50 cm2. This tank is being filled
at the rate of 15 liters per minute. Find the rate at which
the height of the water in the water tank increases; express
your answer in millimeters per second. (Hint: 1 liter = 1000 cm3)

'''
# Rectangular prism volume = l * w * h
# The volume is given in fill rate.  To convert the increase in height
# the formula is to divide the volume/base  (base = length * width)
def rect_prism_vol():
    prism_base_cm2 = 50 # area of base in square cm
    vol_liters_per_min = 15 # volume added in liters, per minute
    # Before we can calculate height gained in mm per second, we need to work our
    # way through some conversions. Start with calculating the volume in cm per
    # minute: multiply the volume in liters by 1000 cm3 per liter:
    vol_cm3_per_min = vol_liters_per_min * 1000
    # For any volume of a rectangular prism, volume = base * height,
    # so, height = volume / base, or
    height_cm_per_min = vol_cm3_per_min / prism_base_cm2
    # Convert height per minute to height per second by dividing by 60:
    height_cm_per_sec = height_cm_per_min / 60 # since 60 seconds per minute
    # Finally, convert height per second in cm to height per second in mm. There
    # are 10 millimeters in a centimeter, so we just multiply by 10:
    height_mm_per_sec = height_cm_per_sec * 10
    print('7. The height of the water is increasing at', height_mm_per_sec, 'mm/s.')

# coverting minutes into seconds * 60

exitonclick()

