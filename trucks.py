import datetime
from csvReader import addressList, distanceList, packageList
from packages import packageHash, insertPackages, Package


# Truck Class with it's associated functions
class Trucks:
    def __init__(self, speed, miles, currentLocation, departTime, packageIds):
        self.speed = speed
        self.miles = miles
        self.currentLocation = currentLocation
        self.departTime = departTime
        self.currentTime = departTime
        self.packageIds = packageIds

    def __str__(self):
        return f"{self.speed}, {self.miles}, {self.currentLocation}, {self.currentTime}, {self.departTime}, {self.packageIds}"

def minDistance(address):
    for row in addressList:
        if address in row[2]:
            return int(row[0])


def distanceBetween(address1, address2):
    distance = distanceList[address1][address2]
    if distance == '':
        distance = distanceList[address2][address1]
    return float(distance)

insertPackages(packageHash)

truck1 = Trucks(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8), [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40])
truck2 = Trucks(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=11), [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38])
truck3 = Trucks(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=12), [6,7,8,10,11,12,17,21,22,23,24,25,33,39])


def deliverPackages(truck):
    enroutePackages = []
    for packageID in truck.packageIds:
        package = packageHash.search(packageID)
        enroutePackages.append(package)

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

        if nextPackage:
            enroutePackages.remove(nextPackage)
            truck.packageIds.append(nextPackage.id)
            truck.miles += nextAddress
            truck.currentLocation = nextPackage.address
            truck.currentTime += datetime.timedelta(hours=nextAddress/truck.speed)
            nextPackage.delTime = truck.currentTime
            nextPackage.departureTime = truck.departTime

deliverPackages(truck1)
deliverPackages(truck2)

print("The total miles the truck traveled is: ", truck2.miles)