import datetime
from csvReader import addressList, distanceList, packageList
from packages import packageHash, insertPackages, Package


# Truck Class with it's associated functions
class Trucks:
    def __init__(self, speed, miles, currentLocation, departTime, packageIds, truckNumber = None):
        self.speed = speed
        self.miles = miles
        self.currentLocation = currentLocation
        self.departTime = departTime
        self.currentTime = departTime
        self.packageIds = packageIds
        self.truckNumber = truckNumber

    def __str__(self):
        return f"{self.speed}, {self.miles}, {self.currentLocation}, {self.currentTime}, {self.departTime}, {self.packageIds}, {self.truckNumber}"

#Function that finds the array value of the address and returns it to be used in distance between
def minDistance(address):
    for row in addressList:
        if address in row[2]:
            return int(row[0])

#Pulls the value off the distance table and replaces that distance value if it's less than the original number
def distanceBetween(address1, address2):
    distance = distanceList[address1][address2]
    if distance == '':
        distance = distanceList[address2][address1]
    return float(distance)

insertPackages(packageHash)

truck1 = Trucks(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8), [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40], 1)
truck2 = Trucks(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=11), [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38], 2)
truck3 = Trucks(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=12), [6,7,8,10,11,12,17,21,22,23,24,25,33,39], 3)

#Function that actually delivers the packages. Creates a list for each truck and appends the packages for each truck to the list.
def deliverPackages(truck):
    enroutePackages = []
    for packageID in truck.packageIds:
        package = packageHash.search(packageID)
        enroutePackages.append(package)

    #While / For Loops to run through all the distances of the packages on each truck to find the closest location to go to next.
    while enroutePackages:
        nextAddress = float('inf')
        nextPackage = None
        for package in enroutePackages:
            if package.id in [25, 6]:
                nextPackage = package
                nextAddress = distanceBetween(minDistance(truck.currentLocation), minDistance(package.address))
                break
            secondaryAddress = distanceBetween(minDistance(truck.currentLocation), minDistance(package.address))
            if secondaryAddress <= nextAddress:
                nextAddress = secondaryAddress
                nextPackage = package

        #Conditional statement that removes the package from the en route list once the package has been delivered.
        #It then updates the miles for the truck, updates the current time, the delivery time of the package
        #and pushes the loop back up to see if there's more packages to be delivered.
        if nextPackage:
            enroutePackages.remove(nextPackage)
            truck.packageIds.append(nextPackage.id)
            truck.miles += nextAddress
            truck.currentLocation = nextPackage.address
            truck.currentTime += datetime.timedelta(hours=nextAddress/truck.speed)
            nextPackage.delTime = truck.currentTime
            nextPackage.departTime = truck.departTime
            nextPackage.truck = truck.truckNumber