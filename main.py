#Name: Dillan Firth-Klute
#Student ID: 001488123
#Class: C950 - Data Structures and Algorithms II


from datetime import datetime, timedelta
from packages import packageHash, insertPackages, Package
from trucks import truck1, truck2, truck3, deliverPackages

#Delivering packages on Truck 1
deliverPackages(truck1)

#Delivering packages on Truck 3
deliverPackages(truck3)

#Finding the earliest one of the trucks return to the warehouse
#as only 2 trucks can be gone at the same time. Changing the value of
#package 9 inversely, and outside the object, so when we look the package up
#it's not actually updating the object permanently
truck2.departTime = min(truck2.departTime, truck3.departTime)
packageHash.search(9).address = "410 S State St"
packageHash.search(9).zip = "84111"
deliverPackages(truck2)

#Function to get user's input for the package ID they want to search for
def getPackageID():
    try:
        package = int(input("Please enter a package ID: "))
        return [package]
    except ValueError:
        return range(1, 41)

#Function to get user's input for the time they want to search for
def getTime():
    time = input("Please enter a time (HH:MM): ")
    (h, m) = time.split(':')
    return timedelta(hours=int(h), minutes=int(m))

#Function that changes the package color based on the status of the package
def statusColor(status):
    color = {
        "At the Hub": "\033[91m",
        "En Route": "\033[93m",
        "Delivered": "\033[92m"
    }
    return color.get(status, "\033[0m")

#Function for Option 2: Getting package status based on the user's ID and Time input
# and changes the color of the output based on the package's status
def option2(packageID, updatedTime):
    for packageID in packageID:
        packageSearch = packageHash.search(packageID)
        print(f"{header}")
        status, printstr = packageSearch.packageStatus(updatedTime)
        print(statusColor(status) + printstr + "\033[0m")
    print("\n\n")

#Function for Option 3: Getting the package status based on the user's time input
# and changing the color of the output based on the package's status
def option3(updatedTime):
    print(f"{header}")
    for bucket in packageHash.table:
        for key, _ in bucket:
            packageSearch = packageHash.search(key)
            status,printstr = packageSearch.packageStatus(updatedTime)
            print(statusColor(status) + printstr + "\033[0m")
    print("\n\n")

#Creating header for the UI
header = (
        "ID   ||    ADDRESS      ||   CITY   ||  STATE  ||  ZIPCODE  || "
        "DEADLINE || WEIGHT (KILO) || SPECIAL NOTES || PACKAGE STATUS || DEPARTURE TIME || DELIVERY TIME || TRUCK NUMBER: ")

#User Interface
print("\n\nWELCOME TO WESTERN GOVERNORS UNIVERSITY PARCEL SERVICE")
print("The Total Miles the Trucks Traveled is: ", truck1.miles + truck2.miles + truck3.miles, "\n\n")

while True:
    optionInput = input(f"Please pick from the following options:\n"
          f"1) Print all packages with their attributes:\n"
          f"2) Print a single package for a specific time:\n"
          f"3) Print all packages for a specific time: ")

    #Option 1: Print all packages w/ their attributes
    if optionInput == "1":
        print(f"\n\n{header}")
        for bucket in packageHash.table:
            for key, _ in bucket:
                print(packageHash.search(key))
        print("\n\n")

    #Option 2: Single Package for a specific time
    if optionInput == "2":
        package = getPackageID()
        time = getTime()
        option2(package, time)

    #Option 3: All Packages for a specific time
    if optionInput == "3":
        time = getTime()
        option3(time)

