import asyncio

async def main():
    print('Hello ...You have 5 seconds to get the correct answer.')
    print('If you do not choose correctly you lose the game.')
    num = 5
    task2 = asyncio.create_task(game())
    while num >= 1:
        await asyncio.sleep(1)
        print(num)
        num -= 1
    print('you lose')
        
            
async def game():
    answer = input('What is the meaning of the life?') 
    if answer == '42':
        print('You are correct')
    elif answer != '42':
        thing()
        
def thing():
    pass
    
        

asyncio.run(main())


