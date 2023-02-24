#mhttps://github.com/users/Kevinhayforn
#Script for car prices
#prices of cars are in US dollars
# Script for car prices
# Prices of cars are in US dollars

car_prices = {
    'ford': 4500,
    'tesla': 6000,
    'nissan': 28000,
    'jeep': 85400,
    'toyotaAstraMotor': 15000,
    'jaguar': 48000,
    'volvo': 12000,
    'landRover': 35000,
    'mitsubishi': 70000,
    'buick': 92000,
    'porche': 83500,
    'volkswagen': 13000,
    'chevrolet': 56000,
    'rangeRover': 2000,
    'bugatti': 39000,
    'rollsRoyce': 9000,
    'ferrari': 89000,
    'lamborghini': 99000,
    'pagani': 50000,
    'astonMartin': 30000,
    'mazda': 21000,
    "Toyota Corolla": 30000,
    "Lamborghini": 95000,
    "SUV":35000,
    "Ford Explorer":50000,
    "McLauren":9500,
    "ferrari laferrari":7099,
    "mclauren pi":9009,
    "porsche918 spyder":78898,
    "koenigsegg regera":96959,
    "huracan performante":96959,
    "paganin huayra roadster":933948,
    "senna":46876,
    "sf90 stradule":78876,
    "bugatti chiron":87657,
    "ssc tuatara":985445,
    "aston martin valkyrie":549549,
    "toyota":857847,
}

car_brand = input('hello welcome to Ebo car dealership please enter car brand: ').lower()

if car_brand in car_prices:
    print(f"The price of {car_brand} is ${car_prices[car_brand]:,}")
else:
    print(f"Sorry, {car_brand} is not in our list thank you.")
if car_brand in car_prices:
    print("thank u for dealing with ebo dealership")