import math
import sys
import os

def load_inputs():
    file = open("day1input.txt", "r")
    
    masses = []
    for aline in file:
        aline = int(aline.strip())
        masses.append(aline)

    file.close()
    return masses


def get_fuelcost(masses):
    fuelcost = []
    for mass in masses:
        fuel = (mass // 3) - 2
        fuelcost.append(fuel)

    return fuelcost


def get_fuelcostoffuel(fuelcost):
    for location, fuel in enumerate(fuelcost):
        fuelfuelcost = (fuel // 3) - 2
        while fuelfuelcost >= 0:
            fuel = fuel + fuelfuelcost
            fuelfuelcost = (fuelfuelcost // 3) - 2
        fuelcost[location] = fuel
    
    return fuelcost
        

def get_totalfuelcost(fuelcost):
    total = 0
    for fuel in fuelcost:
        total = total + fuel
    return total

def main():
    masses = load_inputs()
    fuelcost = get_fuelcost(masses)
    fuelcost = get_fuelcostoffuel(fuelcost)
    total = get_totalfuelcost(fuelcost)
    print(total)

main()