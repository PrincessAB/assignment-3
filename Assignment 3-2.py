#car dealership, toyota car, benz etc, which has a sale price, write a code that ask the person purchase in a car, the brand that he wants.
#2882120 
#Github username = PrincessAB
#https://github.com/PrincessAb/Data-Structures
print("Akwaaba! in other words welcome to AB's motors, we proudly offer exuberant and affordable industry leading cars to your satisfaction. Find your perfect vehicle and test drive today!" )
fleet_of_cars = {'Range Velar' : 100000, 'Range Evoque' : 351000, 'Range Sports' : 413000, 'Range Discovery' : 493000,  
                 'Mercedes benz C300' : 410000, 'Mercedes benz S650' : 520000, 'Mercedes benz Sls 65 Amg' : 651000, 
                 'Lexus RX350' : 720000, 'Lexus LX570' : 810000, 'Lexus LFA' : 915000, 
                 'Toyota Yaris' : 24000, 'Toyota Vitz' : 25000, 'Toyota Tundra' : 4000,
                 'Aston Martin DB11' : 217000, 'Aston Martin Vanquish' : 312000, 'Aston martin DB9' : 300000 , 
                 'Bentely Bentayga' : 512000, 'Bentely Continental' : 211000, 'Bentely Mulsanne' : 310000,
                 'Infinity QX80' : 334000, 'Infinity QX56' : 423000, 'Infinity G37': 521500,
                 'Tesla Model S' : 630000, 'Tesla Model X' : 120000, 'Tesla Model Y' : 712000,
                 'Ferrari F40' : 615300, 'Ferrari Enzo' : 712250, 'Ferrari 458 Italia' : 813400,
                 'Ford Focus' : 16000, 'Ford GT': 450000}
choice_made = input('HELLO, I am Abena at your service. Please what is your preference of car today? : ')
if choice_made in fleet_of_cars:
    print() #leaving space in between 
    print('That is a spectacular choice. I assure you, you will find the price worth the car. ')
    print('That will be.. USD ' + str(fleet_of_cars[choice_made]))
else: 
    print('Sorry Sir/Madame, unfortunately we do not have that car in stock currently. We will be sure to make it available to you on your next visit')
    
    
